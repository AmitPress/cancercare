from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .models import RegisterAmbulanceMember, DrugInfo, Volunteer, Specialist, Comment, Post
from .forms import RegisterAmbulanceMemberForm, VolunteerForm, SpecialistForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import sys
sys.path.append("..")
from auths.models import UserProfile
# Create your views here.

class RegisterAmbulanceMemberFormView(CreateView):
    model = RegisterAmbulanceMember
    form_class = RegisterAmbulanceMemberForm
    template_name = 'mainfeatures/register_ambulance_feature.html'

class VolunteerView(CreateView):
    model = Volunteer
    form_class = VolunteerForm
    template_name = 'mainfeatures/register_volunteer.html'
class SpecialistView(CreateView):
    model = Specialist
    form_class = SpecialistForm
    template_name = 'mainfeatures/register_specialist.html'

class DrugListView(ListView):
    model = DrugInfo
    template_name = 'mainfeatures/druginfo_list.html'
    paginate_by = 5
    # queryset = DrugInfo.objects.all()

# implement drug search
def search_drug(request):
    query = request.GET['search_drug']
    lists = DrugInfo.objects.filter(drugname__icontains=query)
    return render(request, 'mainfeatures/druginfo_list.html', {'object_list':lists})

def forum(request):
    comments = Comment.objects.all().order_by('-timestamp__date').order_by('-timestamp__time')
    comment_count = Comment.objects.all().count()
    paginator = Paginator(comments, 4)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    comobj = {
        'comments': page_obj,
        'count': comment_count

    }
    return render(request, 'mainfeatures/forum.html', {'comobj':comobj})

def comment(request):
    if request.method == 'POST':
        cmnt = request.POST['comment']
        # have to have a model for comment 
        if str(request.user) == 'AnonymousUser':
            messages.error(request, 'failed to comment; you have to login first')
            return redirect('/forum')
        else:
            usr = request.user
            cmnt_obj = Comment(body=cmnt, user=usr)
        
        
        cmnt_obj.save()
        messages.success(request, 'Your comment is added successfully')
    return redirect('/forum')

def updates(request):
    posts = Post.objects.all().order_by('-timestamp__date').order_by('-timestamp__time')
    post_count = Post.objects.all().count()
    profile = UserProfile.objects.get(user=request.user)
    paginator = Paginator(posts, 4)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    ctx = {
        'posts':page_obj,
        'post_count':post_count,
        'profile':profile
    }
    return render(request, 'mainfeatures/updates.html', ctx)
def deletepost(request, delete_post):
    Post.objects.get(serial_no=delete_post).delete()
    return redirect('/updates')
def postbody(request, slug):
    post = Post.objects.filter(slug=slug).first()
    ctx = {
        'post':post
    }
    return render(request, 'mainfeatures/postbody.html', ctx)
# get userprofile
def compounder(request):
    compounders = UserProfile.objects.filter(role='compounder')
    return render(request, 'mainfeatures/compounders.html', {'compounders':compounders})

    
    
