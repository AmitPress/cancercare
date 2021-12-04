from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import RegisterAmbulanceMember, DrugInfo, Volunteer

# Create your views here.

class RegisterAmbulanceMemberFormView(CreateView):
    model = RegisterAmbulanceMember
    template_name = 'mainfeatures/register_ambulance_feature.html'
    fields = '__all__'

class VolunteerView(CreateView):
    model = Volunteer
    template_name = 'mainfeatures/register_volunteer.html'
    fields = '__all__'

class DrugListView(ListView):
    model = DrugInfo
    template_name = 'mainfeatures/druginfo_list.html'
