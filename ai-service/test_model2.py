import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# 1. Load the EfficientNet Brain
print("Loading model...")
model = load_model('cattle_final_v3.h5') 

# 2. Load and Prep Image
# EfficientNet expects pixels 0-255. Do NOT divide by 255.
img = image.load_img('./testImages/hariana.jpeg', target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) # Shape: (1, 224, 224, 3)

# 3. Predict
predictions = model.predict(img_array)

# --- FIX IS HERE ---
# The model output is ALREADY the score. Do not use tf.nn.softmax again.
score = predictions[0] 

predicted_class_id = np.argmax(score)
confidence = 100 * np.max(score)

# 4. Result
print(f"\n------------------------------------------------")
print(f"RAW PREDICTION SCORES: {score}") # Verify the raw numbers
print(f"------------------------------------------------")
print(f"I am {confidence:.2f}% sure this is Class ID: {predicted_class_id}")
print(f"------------------------------------------------")