from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class RegisterAmbulanceMember(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    fulname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
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
    phone = models.CharField(max_length=255)
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
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=512)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    serial_no = models.AutoField(primary_key=True)
    body = models.CharField(max_length=256)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    parent = models.ForeignKey("self",on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.body[0:15]+'... by '+ self.user.username

class Post(models.Model):
    serial_no = models.AutoField(primary_key=True)
    author = models.CharField(max_length=30)
    ptype = models.CharField(max_length=10)
    title = models.CharField(max_length=40)
    slug = models.CharField(max_length=30)
    body = models.TextField()
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.body[0:15]+'... by '+ self.author