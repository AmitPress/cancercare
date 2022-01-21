from django.contrib import admin
from .models import RegisterAmbulanceMember, DrugInfo, Volunteer, Specialist, Comment, Post
# Register your models here.
admin.site.register(RegisterAmbulanceMember)
admin.site.register(DrugInfo)
admin.site.register(Volunteer)
admin.site.register(Specialist)
admin.site.register(Comment)
admin.site.register(Post)