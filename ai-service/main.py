from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
from tensorflow.keras.models import load_model

app = FastAPI()

# 1. SETUP
print("⏳ Loading EfficientNet Model...")
# Ensure this matches your file name exactly
model = load_model('cattle_final_v3.h5') 
print("✅ Model Loaded!")

# 2. CLASS NAMES (Must match your Colab Alphabetical Order)
CLASS_NAMES = [
    'Deoni',        # 0
    'Gir',          # 1
    'Hariana',      # 2
    'Jaffrabadi',   # 3 
    'Kangayam',     # 4
    'Kankrej',      # 5
    'Murrah',       # 6 
    'Rathi',        # 7
    'Red_Sindhi',   # 8
    'Sahiwal'       # 9
]

def read_file_as_image(data) -> np.ndarray:
    # Resize to 224x224, RAW PIXELS (0-255)
    image = np.array(Image.open(BytesIO(data)).resize((224, 224)))
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0) # Create batch

    # Run AI
    predictions = model.predict(img_batch)
    score = predictions[0]  # Get probability array
    
    # Find Winner
    class_id = np.argmax(score)
    confidence = np.max(score) * 100
    result_name = CLASS_NAMES[class_id]
    
    # Console Log for Debugging
    print(f"PREDICTION: {result_name} ({confidence:.2f}%)")

    return {
        'class': result_name,
        'confidence': float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)