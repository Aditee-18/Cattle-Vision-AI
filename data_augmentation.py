import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

# ================= CONFIGURATION =================
# 1. Path to your dataset folder
DATASET_DIR = "images"  # Make sure this matches your folder name

# 2. How many images do you want PER CLASS?
# If you have 80 Gir cows, this will create 420 new ones to reach 500.
TARGET_COUNT = 500 
# =================================================

# Define the transformations (The "Augmentation")
datagen = ImageDataGenerator(
    rotation_range=30,      # Rotate image up to 30 degrees
    width_shift_range=0.2,  # Shift left/right
    height_shift_range=0.2, # Shift up/down
    shear_range=0.2,        # Slant the image
    zoom_range=0.2,         # Zoom in/out
    horizontal_flip=True,   # Mirror image
    fill_mode='nearest'     # Fill empty space with nearest color
)

print(f"Starting Augmentation... Target: {TARGET_COUNT} images per breed.\n")

classes = [d for d in os.listdir(DATASET_DIR) if os.path.isdir(os.path.join(DATASET_DIR, d))]

for breed in classes:
    breed_path = os.path.join(DATASET_DIR, breed)
    
    # Get list of all images in this breed folder
    images = [os.path.join(breed_path, f) for f in os.listdir(breed_path) 
              if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    current_count = len(images)
    print(f"Processing {breed}: Found {current_count} images.")
    
    if current_count == 0:
        print(f"Skipping {breed} (Empty folder)")
        continue
        
    if current_count >= TARGET_COUNT:
        print(f"  -> Sufficient data. Skipping.")
        continue

    # Calculate how many to generate
    needed = TARGET_COUNT - current_count
    print(f"  -> Generating {needed} new images...")

    # We loop through existing images and generate new ones
    generated_count = 0
    
    while generated_count < needed:
        for img_path in images:
            if generated_count >= needed:
                break
                
            try:
                # Load the image
                img = load_img(img_path) 
                x = img_to_array(img)
                x = x.reshape((1,) + x.shape) # Reshape to (1, height, width, channels)

                # Create 1 augmented image and save it to the SAME folder
                for batch in datagen.flow(x, batch_size=1, 
                                          save_to_dir=breed_path, 
                                          save_prefix='aug', 
                                          save_format='jpg'):
                    generated_count += 1
                    break # Stop the internal loop, move to next image
            except Exception as e:
                print(f"    Error on image {img_path}: {e}")

    print(f"  -> Done. Total {breed} is now {len(os.listdir(breed_path))}")

print("\nAll Done! Your dataset is now massive.")