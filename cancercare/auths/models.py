from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    # We use this foreign key to link the user profile to the appropriate user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)