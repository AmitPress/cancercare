from django.urls import path
from .views import home, signup

urlpatterns = [
    path('home/', home, name='home'),
    path('signup/', signup, name='signingup')
]