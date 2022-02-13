from django import forms
from django.contrib.auth import get_user_model
from product.models import Products



class ProductForm(forms.ModelForm): 
    class Meta:
        model = Products
        fields = ("__all__")
        