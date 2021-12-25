from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile')
]

# Now I wanna change something in your view
# You see, when importing various functions or classes from the same file, just import the file itself
# I.E. You're importing three functions from the views file. Instead of importing them individually, just import the file itself
# Let me show you
# The only time this is necessry is when yiu are importing multiple functions