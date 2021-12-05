from django import forms
from .models import RegisterAmbulanceMember, Volunteer, Spcialist

class RegisterAmbulanceMemberForm(forms.ModelForm):
    class Meta:
        model = RegisterAmbulanceMember
        fields = ('fname', 'lname', 'fulname', 'phone', 'address', 'age')
        widgets = {
            'fname' : forms.TextInput(attrs={'class':'form-control'}),
            'lname' : forms.TextInput(attrs={'class':'form-control'}),
            'fulname'   : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'address'   : forms.Textarea(attrs={'class':'form-control'}),
            'age'   : forms.NumberInput(attrs={'class':'form-control'})
        }
class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('first_name', 'last_name', 'full_name', 'phone', 'address', 'age')
        widgets = {
            'fname' : forms.TextInput(attrs={'class':'form-control'}),
            'lname' : forms.TextInput(attrs={'class':'form-control'}),
            'fulname'   : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'address'   : forms.Textarea(attrs={'class':'form-control'}),
            'age'   : forms.NumberInput(attrs={'class':'form-control'})
        }

class SpecialistForm(forms.ModelForm):
    class Meta:
        model = Spcialist
        fields = ('first_name', 'last_name', 'full_name', 'phone', 'address', 'age')
        widgets = {
            'fname' : forms.TextInput(attrs={'class':'form-control'}),
            'lname' : forms.TextInput(attrs={'class':'form-control'}),
            'fulname'   : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'address'   : forms.Textarea(attrs={'class':'form-control'}),
            'age'   : forms.NumberInput(attrs={'class':'form-control'})
        }