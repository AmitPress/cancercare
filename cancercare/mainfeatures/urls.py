from django.urls import path
from .views import RegisterAmbulanceMemberFormView, DrugListView, VolunteerView, SpecialistView, search_drug,forum
urlpatterns=[
    path('register-ambulance/', RegisterAmbulanceMemberFormView.as_view(), name="register-ambulance"),
    path('druglist/', DrugListView.as_view(), name="druglist"),
    path('register-volunteer/', VolunteerView.as_view(), name="registervolunteer"),
    path('register-specialist/', SpecialistView.as_view(), name="registerspcialist"),
    path('search/', search_drug, name='search'),
    path('forum/', forum, name='forum')
]