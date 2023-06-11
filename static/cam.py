import sys 
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np

classifier = tf.keras.models.load_model('static/model.h5')

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

image_path = 'static/todays_selfie.jpg'  # Provide the path to the image file

# Load and preprocess the image
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (48, 48), interpolation=cv2.INTER_AREA)

# Preprocess the image for the model
roi = gray.astype('float') / 255.0
roi = img_to_array(roi)
roi = np.expand_dims(roi, axis=0)

# Make a prediction on the image
prediction = classifier.predict(roi)
label = emotion_labels[np.argmax(prediction)]

# Save the predicted emotion to a file
emotion_file_path = 'static/emotion.txt'
with open(emotion_file_path, 'w') as file:
    file.write(label)
