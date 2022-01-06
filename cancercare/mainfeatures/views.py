from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import RegisterAmbulanceMember, DrugInfo, Volunteer, Specialist
from .forms import RegisterAmbulanceMemberForm, VolunteerForm, SpecialistForm
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
    
    return render(request, 'mainfeatures/forum.html', {})

    
    
