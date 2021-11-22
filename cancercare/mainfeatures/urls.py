from django.urls import path
from .views import RegisterAmbulanceMemberFormView, DrugListView
urlpatterns=[
    path('register-ambulance/', RegisterAmbulanceMemberFormView.as_view(), name="register-ambulance"),
    path('druglist/', DrugListView.as_view(), name="druglist")
]