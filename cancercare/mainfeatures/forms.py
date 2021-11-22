from django import forms
from .models import RegisterAmbulanceMember

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