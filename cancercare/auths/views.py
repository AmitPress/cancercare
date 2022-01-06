from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .models import UserProfile
import sys
sys.path.append("..")
from mainfeatures.models import RegisterAmbulanceMember, Volunteer, Specialist
# Create your views here.

def signup(request):
    if request.method == "POST":
        # username = request.POST.get('lname') + request.POST.get('fname')
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = fname+' '+lname
        email = request.POST['emailf']
        phone = request.POST['phone']
        pass1 = request.POST['pass']
        pass2 = request.POST['repass']
        thisuser = User.objects.create_user(username, email, pass1)
        thisuser.first_name = fname
        thisuser.last_name = lname
        thisuser.phone = phone
        thisuser.save()
        # After we successfully create the user, we will create the user profile
        # Added UserProfile -- 
        user_profile = UserProfile.objects.create(user=thisuser, role='user', phone=phone) ## lets make it user rather..
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

# Now lets create the view for the profile page 
def profile(request):
    # Check if user is logged in
    if request.user.is_authenticated:
        the_profile = UserProfile.objects.get(user=request.user)
        if the_profile.role == 'compounder':
            return render(request, 'auths/compounder_profile.html', {'user_profile': the_profile})
        elif the_profile.role == 'user':
            status = {'rg_amb':True, 'rg_vol':True, 'rg_spe':True}
            rg_amb = RegisterAmbulanceMember.objects.filter(phone__icontains=the_profile.phone)
            if len(rg_amb) is 0:
                status['rg_amb'] = False
            rg_vol = Volunteer.objects.filter(phone__icontains=the_profile.phone)
            if len(rg_vol) is 0:
                status['rg_vol'] = False
            rg_spe =  Specialist.objects.filter(phone__icontains=the_profile.phone)
            if len(rg_spe) is 0:
                status['rg_spe'] = False
            return render(request, 'auths/profile.html', {'user_profile': the_profile, 'user': request.user, 'status':status})
        else:
            messages.error(request, 'Invalid User Role')
            return redirect('login')
        return render(request, 'auths/profile.html') # I am creating the file 'profile.html' in templates
    # Redirect user to login page if the user isnt logged in
    else:
        messages.error(request, "You need to be logged in to view your profile")
        return redirect('login')

    #I have created it already. Look at the templates folder
    # okay then I am addin header and footer in that template
    # Okay. But are you using a base template in your project?

