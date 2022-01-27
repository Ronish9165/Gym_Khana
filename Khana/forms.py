from django import forms
from django.db.models import fields

class UserResgistrationForm(forms.ModelForm): 
    class Meta:
        fields = ["username","first_name","email","password"]
        