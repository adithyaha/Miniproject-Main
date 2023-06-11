import mysql.connector
import subprocess
import sys
from flask import Flask, render_template, request, redirect, session
from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import datetime
import os
import base64
import tensorflow as tf
from flask import jsonify,make_response
from flask import Flask, request, jsonify
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('stopwords')
nltk.download('punkt')

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'adithya',
    'password': '123',
    'database': 'mydatabase'
}

# Recommendation data
recommendations = {
    ((15, 20), 'Female', 'Happy'): "Connect with supportive friends, participate in creative endeavors, and seek opportunities for personal growth and self-expression.",
    ((15, 20), 'Female', 'Sad'): "Seek support from loved ones, practice self-care, and explore therapeutic outlets such as counseling or expressive arts.",
    ((15, 20), 'Female', 'Neutral'): "Focus on self-reflection, engage in mindfulness practices, and pursue activities that nurture your well-being and personal growth.",
    ((15, 20), 'Female', 'Angry'): "Explore anger management strategies, practice effective communication skills, and prioritize self-care activities that promote emotional balance.",
    ((15, 20), 'Female', 'Disgust'): "Educate yourself on environmental and social issues, make sustainable choices, and promote positive change through activism or volunteering.",
    ((15, 20), 'Female', 'Surprise'): "Embrace spontaneity, seek adventure, and pursue opportunities that bring unexpected joy and excitement into your life.",
    ((15, 20), 'Female', 'Fear'): "Embrace your passions, engage in activities that spark joy, and surround yourself with people who inspire and motivate you.",
    
    ((15, 20), 'Male', 'Happy'): "Engage in social activities, join clubs or organizations related to your interests, and pursue personal goals with enthusiasm and positivity.",
    ((15, 20), 'Male', 'Sad'): "Reach out for emotional support, engage in activities that bring joy, and consider seeking professional help to address underlying causes of sadness.",
    ((15, 20), 'Male', 'Neutral'): "Explore various interests, expand your knowledge through learning opportunities, and consider volunteering to find a sense of purpose.",
    ((15, 20), 'Male', 'Angry'): "Find healthy ways to manage anger, such as engaging in physical exercise, practicing relaxation techniques, and seeking guidance to resolve underlying issues.",
    ((15, 20), 'Male', 'Disgust'): "Channel your emotions into advocacy for social causes, support ethical initiatives, and engage in community-building activities.",
    ((15, 20), 'Male', 'Surprise'): "Embrace new experiences, step out of your comfort zone, and cultivate a sense of wonder through exploration and discovery.",
    ((15, 20), 'Male', 'Fear'): "Set ambitious goals, challenge yourself to take risks, and actively pursue opportunities that bring fulfillment and excitement.",
    
    ((21, 35), 'Female', 'Happy'): "Focus on self-care, invest in relationships, and explore new avenues for personal growth and happiness.",
    ((21, 35), 'Female', 'Sad'): "Prioritize self-care, seek professional help if needed, and find solace in activities that nurture emotional well-being.",
    ((21, 35), 'Female', 'Neutral'): "Reflect on personal values and goals, nurture personal growth, and find balance in life.",
    ((21, 35), 'Female', 'Angry'): "Develop healthy coping mechanisms, engage in stress-reducing activities, and focus on building positive relationships.",
    ((21, 35), 'Female', 'Disgust'): "Promote sustainability, support eco-friendly practices, and contribute to organizations working towards positive change.",
    ((21, 35), 'Female', 'Surprise'): "Seek novelty in experiences, explore diverse interests, and prioritize self-discovery and personal growth.",
    ((21, 35), 'Female', 'Fear'): "Embrace opportunities that ignite your passion, nurture a sense of adventure, and cultivate an enthusiastic outlook on life.",
    
    ((21, 35), 'Male', 'Happy'): "Maintain a healthy work-life balance, nurture relationships, and continue pursuing personal and professional growth.",
    ((21, 35), 'Male', 'Sad'): "Seek support from loved ones, consider therapy or counseling, and focus on self-care activities.",
    ((21, 35), 'Male', 'Neutral'): "Rediscover interests and hobbies, seek personal and professional development opportunities, and foster a sense of purpose.",
    ((21, 35), 'Male', 'Angry'): "Practice anger management techniques, seek counseling, and explore healthy outlets like exercise or creative expression.",
    ((21, 35), 'Male', 'Disgust'): "Engage in advocacy and community initiatives, support causes that align with your values, and contribute to positive change.",
    ((21, 35), 'Male', 'Surprise'): "Embrace new opportunities, challenge yourself to try new things, and cultivate a sense of adventure and curiosity.",
    ((21, 35), 'Male', 'Fear'): "Pursue exciting endeavors, take calculated risks, and find ways to infuse passion and enthusiasm into your personal and professional life.",
    
    ((36, 60), 'Female', 'Happy'): "Prioritize self-care, nurture meaningful relationships, and pursue activities that bring you joy and fulfillment.",
    ((36, 60), 'Female', 'Sad'): "Seek emotional support from loved ones, consider therapy or counseling, and focus on activities that promote healing and well-being.",
    ((36, 60), 'Female', 'Neutral'): "Maintain a healthy work-life balance, explore personal interests, and engage in activities that nurture your overall well-being.",
    ((36, 60), 'Female', 'Angry'): "Practice effective communication, explore anger management strategies, and prioritize self-care activities that promote emotional balance.",
    ((36, 60), 'Female', 'Disgust'): "Support causes aligned with your values, engage in advocacy, and contribute to positive change in your community.",
    ((36, 60), 'Female', 'Surprise'): "Embrace new experiences and challenges, foster personal growth and learning, and pursue adventures that ignite your passion.",
    ((36, 60), 'Female', 'Fear'): "Face your fears with courage, seek support from loved ones, and engage in activities that promote self-confidence and security.",
    
    ((36, 60), 'Male', 'Happy'): "Cultivate gratitude, maintain social connections, and pursue joyful and fulfilling activities.",
    ((36, 60), 'Male', 'Sad'): "Seek emotional support, practice self-compassion, and engage in healing activities.",
    ((36, 60), 'Male', 'Neutral'): "Rediscover passions, pursue hobbies, and engage in purposeful activities.",
    ((36, 60), 'Male', 'Angry'): "Seek outlets for anger, practice stress management, and build healthy relationships.",
    ((36, 60), 'Male', 'Disgust'): "Engage in advocacy, support causes you value, and contribute to positive change.",
    ((36, 60), 'Male', 'Surprise'): "Embrace new experiences and challenges, embark on travel adventures, and continue pursuing personal growth and learning.",
    ((36, 60), 'Male', 'Fear'): "Find excitement in new ventures or projects, engage in social activities, and maintain an optimistic outlook.",
    
    ((61, 70), 'Female', 'Happy'): "Nurture your well-being through self-care, maintain social connections, and pursue activities that bring you happiness and fulfillment.",
    ((61, 70), 'Female', 'Sad'): "Seek emotional support from loved ones, engage in therapeutic activities, and prioritize self-care to promote healing and well-being.",
    ((61, 70), 'Female', 'Neutral'): "Focus on maintaining a balanced lifestyle, explore new hobbies or interests, and engage in activities that promote mental and physical well-being.",
    ((61, 70), 'Female', 'Angry'): "Practice patience, engage in stress-reducing activities, and foster positive relationships to promote emotional well-being.",
    ((61, 70), 'Female', 'Disgust'): "Support causes you care about, engage in community initiatives, and find fulfillment in making a positive impact.",
    ((61, 70), 'Female', 'Surprise'): "Embrace new experiences, cultivate curiosity and wonder, and continue learning and growing to find joy and satisfaction.",
    ((61, 70), 'Female', 'Fear'): "Face fears with courage, seek support from loved ones, and engage in activities that promote a sense of security and well-being.",
    
    ((61, 70), 'Male', 'Happy'): "Nurture your physical and mental well-being, maintain social connections, and engage in activities that bring joy and fulfillment.",
    ((61, 70), 'Male', 'Sad'): "Seek emotional support, engage in therapeutic activities, and focus on self-care to promote healing and well-being.",
    ((61, 70), 'Male', 'Neutral'): "Explore new hobbies or interests, seek personal growth opportunities, and maintain a balanced lifestyle.",
    ((61, 70), 'Male', 'Angry'): "Practice stress management techniques, engage in anger-reducing activities, and foster positive relationships.",
    ((61, 70), 'Male', 'Disgust'): "Support causes you believe in, engage in community initiatives, and find fulfillment in making a positive impact.",
    ((61, 70), 'Male', 'Surprise'): "Embrace new experiences, cultivate curiosity, and continue learning and growing to find joy and fulfillment.",
    ((61, 70), 'Male', 'Fear'): "Face fears with courage, seek support from loved ones, and engage in activities that promote a sense of security and well-being.",
    
    ((71, 100), 'Female', 'Happy'): "Focus on self-care, nurture meaningful relationships, and engage in activities that bring joy and contentment.",
    ((71, 100), 'Female', 'Sad'): "Seek support from loved ones, engage in therapeutic activities, and prioritize self-care to promote emotional well-being.",
    ((71, 100), 'Female', 'Neutral'): "Engage in activities that bring a sense of purpose and fulfillment, maintain social connections, and nurture your overall well-being.",
    ((71, 100), 'Female', 'Angry'): "Practice patience and understanding, engage in stress-reducing activities, and foster positive relationships.",
    ((71, 100), 'Female', 'Disgust'): "Support causes you care about, engage in community initiatives, and find fulfillment in making a positive impact.",
    ((71, 100), 'Female', 'Surprise'): "Embrace new experiences, cultivate curiosity, and continue learning and growing to find joy and fulfillment.",
    ((71, 100), 'Female', 'Fear'): "Face fears with courage, seek support from loved ones, and engage in activities that promote a sense of security and well-being.",
    
    ((71, 100), 'Male', 'Happy'): "Prioritize self-care, maintain social connections, and engage in activities that bring joy and contentment.",
    ((71, 100), 'Male', 'Sad'): "Seek emotional support from loved ones, engage in therapeutic activities, and prioritize self-care to promote emotional well-being.",
    ((71, 100), 'Male', 'Neutral'): "Engage in activities that bring a sense of purpose and fulfillment, explore new interests, and nurture your overall well-being.",
    ((71, 100), 'Male', 'Angry'): "Practice patience and understanding, engage in stress-reducing activities, and foster positive relationships.",
    ((71, 100), 'Male', 'Disgust'): "Support causes you care about, engage in community initiatives, and find fulfillment in making a positive impact.",
    ((71, 100), 'Male', 'Surprise'): "Embrace new experiences, cultivate curiosity, and continue learning and growing to find joy and fulfillment.",
    ((71, 100), 'Male', 'Fear'): "Face fears with courage, seek support from loved ones, and engage in activities that promote a sense of security and well-being."
}


def fetch_recommendation_data(username):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Fetch the user's age and gender from the users table
    cursor.execute("SELECT age, gender FROM users WHERE username = %s", (username,))
    user_data = cursor.fetchall()
    age, gender = user_data[0] if user_data else (None, None)

    # Fetch the user's most recent emotion from the current user table for the date
    cursor.execute(f"SELECT emotion FROM {username} WHERE date = CURDATE() ORDER BY id DESC LIMIT 1")
    emotion_row = cursor.fetchall()
    emotion = emotion_row[0][0] if emotion_row else None

    cursor.close()
    conn.close()

    return age, gender, emotion

def generate_recommendation(age, gender, emotion):
    # Recommendation code here
    for key in recommendations:
        age_range, gender_key, emotion_key = key
        min_age, max_age = age_range  # Unpack the age range values
        if min_age <= age <= max_age:
            if gender == gender_key and emotion == emotion_key:
                recommendation = recommendations[key]
                return recommendation  # Return the recommendation

    return None 
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

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Delete the existing file if it exists
    if os.path.exists(image_path):
        os.remove(image_path)

    with open(image_path, 'wb') as file:
        file.write(image_bytes)

    run_model_on_image(image_path)  # Run the model on the saved image

    cursor.close()
    conn.close()

    return 'Image saved on the server.'



@app.route('/recommend')
def recommendation():
    username = session.get('username')
    if username:
        age, gender, emotion = fetch_recommendation_data(username)
        recommendation = generate_recommendation(age, gender, emotion)
        print(age)
        print(gender)
        print(emotion)
        print(recommendation)
        response = make_response(jsonify(recommendation=recommendation))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Allow cross-origin resource sharing
        return response
    else:
        return jsonify(error='User not logged in')


@app.route('/notes', methods=['POST'])
def summarize_notes():
    # Get the text from the form field
    text = request.form.get('message')

    # Tokenizing the text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Creating a frequency table to keep the score of each word
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from the original text
    average = int(sumValues / len(sentenceValue))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.5 * average)):
            summary += " " + sentence

    # Return the summary as a JSON response
    return jsonify({'summary': summary})


@app.route('/track')
def track_entries():
    username = session.get('username')
    if username:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Fetch the last five entries for the user
        cursor.execute(f"SELECT * FROM {username} ORDER BY id DESC LIMIT 5")
        user_entries = cursor.fetchall()

        # Prepare the HTML for the entries
        entries_html = "".join(f"<li>{entry[2]}</li>" for entry in user_entries)

        cursor.close()
        conn.close()
        print(entries_html)
        # Return the entries as a JSON response
        return jsonify(entries=entries_html)
    else:
        return jsonify(error='User not logged in')


@app.route('/index')
def main():
    return render_template('index.html', username=session.get('username'))

if __name__ == '__main__':
    app.run()
