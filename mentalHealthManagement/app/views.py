# appname/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        gender = request.POST['gender']
        dob = datetime.strptime(request.POST['dob'], '%Y-%m-%d').date()
        age = calculate_age(dob)

        # Create a new user object
        user = User.objects.create_user(username=username, password=password)

        # Save additional user information
        user.profile.gender = gender
        user.profile.dob = dob
        user.profile.age = age
        user.profile.save()

        return redirect('login.html')  # Replace 'signup_success' with your success page URL

    return render(request, 'signup.html')

def calculate_age(dob):
    today = datetime.today().date()
    age = today.year - dob.year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        age -= 1
    return age

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Query the database for a user with the given username and password
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            # User not found, display an error message
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})

        # User found, perform any desired action (e.g., redirect to a dashboard)
        return redirect('dashboard')

    return render(request, 'login.html')