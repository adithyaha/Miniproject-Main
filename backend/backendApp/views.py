from django.shortcuts import render

from .models import User



from django.shortcuts import render
from .models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        User.objects.create(username=username, password=password, dob=dob, gender=gender)
        return render(request, 'signup_success.html')
    return render(request, 'signup.html')
