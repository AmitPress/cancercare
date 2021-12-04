from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.

def signup(request):
    if request.method == "POST":
        # username = request.POST.get('lname') + request.POST.get('fname')
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = fname+lname
        email = request.POST['emailf']
        phone = request.POST['phone']
        pass1 = request.POST['pass']
        pass2 = request.POST['repass']
        thisuser = User.objects.create_user(username, email, pass1)
        thisuser.first_name = fname
        thisuser.last_name = lname
        thisuser.save()
        messages.success(request, "Your Account has been Successfully created")
        return redirect('login')

    return render(request, 'auths/signup.html', {})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['passwrd']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            fname = user.first_name
            return render(request, 'auths/login.html' , {'fname':fname})
        else:
            messages.error(request, "Login Failed Bad Credentials")
            return redirect('login')
    return render(request, 'auths/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')