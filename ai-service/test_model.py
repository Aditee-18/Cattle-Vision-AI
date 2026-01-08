#this model is for modbile net v2

# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image

# # 1. Load your Brain
# # Make sure this name matches YOUR downloaded file exactly
# model = load_model('cattle_final_model.h5') 

# # 2. Load the Image
# img = image.load_img('test2.jpeg', target_size=(224, 224))
# img_array = image.img_to_array(img)
# img_array = np.expand_dims(img_array, axis=0)
# img_array = img_array / 255.0  # <--- CRITICAL: Math Normalization

# # 3. Predict
# predictions = model.predict(img_array)
# score = tf.nn.softmax(predictions[0])
# confidence = 100 * np.max(score)

# # 4. Result
# print(f"I am {confidence:.2f}% sure this is Class ID: {np.argmax(score)}")