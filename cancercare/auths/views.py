from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .models import UserProfile
from django.core.paginator import Paginator
import sys
sys.path.append("..")
from mainfeatures.models import RegisterAmbulanceMember, Volunteer, Specialist, Post, DrugInfo


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


def profile(request):
    # Check if user is logged in
    if request.user.is_authenticated:
        the_profile = UserProfile.objects.get(user=request.user)
        if the_profile.role == 'compounder':
            drugs = DrugInfo.objects.all()
            ambulances = RegisterAmbulanceMember.objects.all()
            volunteers = Volunteer.objects.all()
            specialists = Specialist.objects.all()
            # drugs paginator
            paginator1 = Paginator(drugs, 4)
            page_no1 = request.GET.get('page')
            page_obj1 = paginator1.get_page(page_no1)
            # ambulances paginator
            paginator2 = Paginator(ambulances, 4)
            page_no2 = request.GET.get('page')
            page_obj2 = paginator2.get_page(page_no2)
            # volunteers paginator
            paginator3 = Paginator(volunteers, 4)
            page_no3 = request.GET.get('page')
            page_obj3 = paginator3.get_page(page_no3)
            # specialists paginator
            paginator4 = Paginator(specialists, 4)
            page_no4 = request.GET.get('page')
            page_obj4 = paginator4.get_page(page_no4)

            ctx = {
                'user_profile': the_profile,
                'drugs': page_obj1,
                'ambulances': page_obj2,
                'volunteers': page_obj3,
                'specialists': page_obj4
            }
            return render(request, 'auths/compounder_profile.html', ctx)
        elif the_profile.role == 'user':
            status = {'rg_amb':True, 'rg_vol':True, 'rg_spe':True}
            rg_amb = RegisterAmbulanceMember.objects.filter(phone__icontains=the_profile.phone).count()
            if rg_amb == 0:
                status['rg_amb'] = False
            rg_vol = Volunteer.objects.filter(phone__icontains=the_profile.phone).count()
            if rg_vol == 0:
                status['rg_vol'] = False
            rg_spe =  Specialist.objects.filter(phone__icontains=the_profile.phone).count()
            if rg_spe == 0:
                status['rg_spe'] = False
            ctx = {
                'user_profile': the_profile,
                'status': status
            }
            return render(request, 'auths/profile.html', ctx)
        else:
            messages.error(request, 'Invalid User Role')
            return redirect('login')
        return render(request, 'auths/profile.html') 
    else:
        messages.error(request, "You need to be logged in to view your profile")
        return redirect('login')

def createpost(request):
    if request.method == 'POST':
        author = request.POST['author']
        ptype = request.POST['ptype']
        title = request.POST['title']
        slug = request.POST['slug']
        body = request.POST['body']
        post = Post.objects.create(author=author, ptype=ptype, title=title, slug=slug, body=body)
        if not post is None:
            post.save()
        else:
            messages.error(request, 'Could not create post!!!')
    else:
        messages.error(request, 'Could not create post!!!')
        render(request, 'auths/createpost.html')
    the_profile = UserProfile.objects.get(user=request.user)
    ctx = {
        'profile':the_profile
    }
    return render(request, 'auths/createpost.html', ctx)


def deletedrug(request, delete):
    cnt = DrugInfo.objects.filter(drugname=delete).count()
    if cnt == 1:
        DrugInfo.objects.get(drugname=delete).delete()
    else:
        DrugInfo.objects.filter(drugname=delete).delete()

    return redirect('/profile')
def createdrug(request):
    if request.method == 'POST':
        drugname = request.POST["Drugname"]
        drugprice = request.POST["Drugprice"]
        manufacturer = request.POST["Manufacturer"]
        availability = request.POST["Availability"]
        print(manufacturer)
        drug = DrugInfo.objects.create(drugname=drugname, drugprice=drugprice, manufacturer=manufacturer, availability=availability)
        drug.save()
    else:
        redirect('/profile')
    return redirect('/profile')

def deleteambulance(request, delete):
    cnt = RegisterAmbulanceMember.objects.filter(fulname=delete).count()
    if cnt == 1:
        RegisterAmbulanceMember.objects.get(fulname=delete).delete()
    else:
        RegisterAmbulanceMember.objects.filter(fulname=delete).delete()

    return redirect('/profile')

def deletevolunteer(request, delete):
    cnt = Volunteer.objects.filter(first_name=delete).count()
    if cnt == 1:
        Volunteer.objects.get(first_name=delete).delete()
    else:
        Volunteer.objects.filter(first_name=delete).delete()

    return redirect('/profile')

def deletespecialist(request, delete):
    cnt = Specialist.objects.filter(first_name=delete).count()
    if cnt == 1:
        Specialist.objects.get(first_name=delete).delete()
    else:
        Specialist.objects.filter(first_name=delete).delete()

    return redirect('/profile')
