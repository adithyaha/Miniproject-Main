import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(r'D:\Data\Desktop\Emotion_Detection_CNN-main\haarcascade_frontalface_default.xml')
classifier = tf.keras.models.load_model(r'D:\Data\Desktop\Emotion_Detection_CNN-main\model.h5')

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

image_path = 'D:/Data/Pictures/Camera Roll/happy (2).jpg'  # Provide the path to the image file

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

# Display the predicted label
print("Predicted Emotion:", label)

# Display the image with the predicted label
cv2.putText(image, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('Emotion Detector', image)
cv2.waitKey(0)
cv2.destroyAllWindows()