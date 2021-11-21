from django.shortcuts import render
from .forms import SignUp

def home(request):
    return render(request, 'landingpage/home.html', {})