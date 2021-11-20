from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'landingpage/home.html', {})
def signup(request):
    return render(request, 'landingpage/usersignup.html', {})