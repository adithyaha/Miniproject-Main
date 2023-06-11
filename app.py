from flask import Flask, render_template, request, redirect, session
import datetime
import os
import base64
import mysql.connector
import subprocess
import sys 
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'adithya',
    'password': '123',
    'database': 'mydatabase'
}




def run_model_on_image(image_path):
    face_cascade_path = os.path.join(app.root_path, 'static', 'haarcascade_frontalface_default.xml')
    classifier_path = os.path.join(app.root_path, 'static', 'model.h5')

    face_classifier = cv2.CascadeClassifier(face_cascade_path)
    classifier = tf.keras.models.load_model(classifier_path)

    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

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

    # Store the emotion in the database
    username = session.get('username')
    if username:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        today = datetime.date.today()
        cursor.execute(f"INSERT INTO {username} (date, emotion) VALUES (%s, %s)", (today, label))
        conn.commit()

        cursor.close()
        conn.close()


@app.route('/')
def index():
    return redirect('/signup')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        dob = request.form['dob']

        # Calculate age from dob
        birth_date = datetime.datetime.strptime(dob, '%Y-%m-%d')
        today = datetime.date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        # Check if the username already exists
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            return render_template('signup.html', error_message='Username already exists.')

        # Insert the new user into the users table with age
        cursor.execute('INSERT INTO users (username, password, gender, dob, age) VALUES (%s, %s, %s, %s, %s)',
                       (username, password, gender, dob, age))
        conn.commit()

        # Create a table for the user
        cursor.execute(f'''
            CREATE TABLE {username} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                date DATE NOT NULL,
                emotion VARCHAR(255),
                notes TEXT
            )
        ''')
        conn.commit()

        cursor.close()
        conn.close()

        return redirect('/login')
    else:
        return render_template('signup.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()  # Fetch the user from the result

        cursor.close()
        conn.close()

        if user:
            session['username'] = username  # Store username in session
            return redirect('/index')
        else:
            return render_template('login.html', error_message='Invalid username or password.')
    else:
        return render_template('login.html', error_message='Please enter valid credentials')



@app.route('/camera')
def camera():
    return render_template('camera.html')



@app.route('/save_image', methods=['POST'])
def save_image():
    image_data = request.json['imageDataURL']
    image_data = image_data.split(',')[1]  # Remove the "data:image/png;base64," prefix

    image_bytes = base64.b64decode(image_data)

    image_path = os.path.join(app.root_path, 'static', 'todays_selfie.jpg')

    # Delete the existing file if it exists
    if os.path.exists(image_path):
        os.remove(image_path)

    with open(image_path, 'wb') as file:
        file.write(image_bytes)

    run_model_on_image(image_path)  # Run the model on the saved image

    return 'Image saved on the server.'

@app.route('/index')
def main():
    return render_template('index.html')

if __name__ == '__main__':

    app.run()