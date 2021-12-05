from django.db import models
from django.urls import reverse
# Create your models here.
class RegisterAmbulanceMember(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    fulname = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=512)
    age = models.IntegerField()

    def __str__(self):
        return self.fulname
    def get_absolute_url(self):
        return reverse('home')

class DrugInfo(models.Model):
    drugname = models.CharField(max_length=255)
    drugprice = models.IntegerField()
    availability = models.CharField(max_length=5)
    manufacturer = models.CharField(max_length=255)

    def __str__(self):
        return self.drugname
    def get_absolute_url(self):
        return reverse('home')
class Volunteer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = str(first_name) + str(last_name)
    phone = models.IntegerField()
    address = models.CharField(max_length=512)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse('home')
class Specialist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = str(first_name) + str(last_name)
    phone = models.IntegerField()
    address = models.CharField(max_length=512)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse('home')
