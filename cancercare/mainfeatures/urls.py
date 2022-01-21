from django.urls import path
from .views import RegisterAmbulanceMemberFormView, DrugListView, VolunteerView, SpecialistView, search_drug, forum, comment, updates, deletepost, postbody, compounder
urlpatterns=[
    path('updates/<str:slug>', postbody, name='postbody'),
    path('register-ambulance/', RegisterAmbulanceMemberFormView.as_view(), name="register-ambulance"),
    path('druglist/', DrugListView.as_view(), name="druglist"),
    path('register-volunteer/', VolunteerView.as_view(), name="registervolunteer"),
    path('register-specialist/', SpecialistView.as_view(), name="registerspcialist"),
    path('search/', search_drug, name='search'),
    path('forum/', forum, name='forum'),
    path('comment/', comment, name='comment'),
    path('compounders/', compounder, name='compounders'),
    path('updates/', updates, name='updates'),
    path('deletepost/<delete_post>', deletepost, name='deletepost'),

]