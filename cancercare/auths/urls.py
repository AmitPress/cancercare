from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/createpost/', views.createpost, name='createpost'),
    path('deletedrug/<delete>', views.deletedrug, name="deletedrug"),
    path('deleteambulance/<delete>', views.deleteambulance, name="deleteambulance"),
    path('deletevolunteer/<delete>', views.deletevolunteer, name="deletevolunteer"),
    path('deletespecialist/<delete>', views.deletespecialist, name="deletespecialist"),
    path('createdrug/', views.createdrug, name="createdrug"),
]
