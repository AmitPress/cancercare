from django.contrib import admin
from .models import RegisterAmbulanceMember, DrugInfo, Volunteer
# Register your models here.
admin.site.register(RegisterAmbulanceMember)
admin.site.register(DrugInfo)
admin.site.register(Volunteer)