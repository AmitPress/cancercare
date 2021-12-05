from django.contrib import admin
from .models import RegisterAmbulanceMember, DrugInfo, Volunteer, Specialist
# Register your models here.
admin.site.register(RegisterAmbulanceMember)
admin.site.register(DrugInfo)
admin.site.register(Volunteer)
admin.site.register(Specialist)