from django.shortcuts import render
from .forms import SignUp

def home(request):
    return render(request, 'landingpage/home.html', {})
def signup(request):
    su = SignUp()
    return render(request, 'landingpage/usersignup.html', {'form':su})