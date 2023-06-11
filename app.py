from flask import Flask, render_template, request, redirect, session
import datetime
import os
import base64
import mysql.connector

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'adithya',
    'password': '123',
    'database': 'mydatabase'
}

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

    return 'Image saved on the server.'


@app.route('/index')
def main():
    return render_template('index.html')

if __name__ == '__main__':

    app.run()