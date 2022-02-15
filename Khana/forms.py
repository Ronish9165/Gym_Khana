from django import forms
from django.contrib.auth import get_user_model
from django.db.models import fields
from Khana.models import Blogs
User = get_user_model()

class UserResgistrationForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ["username","first_name","email","password"]
        widgets = {
            'password': forms.PasswordInput()
        }

    def get_id(self):
        return self.user.id

# class AddressForm(forms.Form):
#     Email = forms.EmailField()
#     Mobile= forms.IntegerField()
#     Address = forms.CharField(max_length=500)

class BlogForm(forms.ModelForm): 
    class Meta:
        model = Blogs
        fields = ["blog_name","blog_details","blog_image"]     