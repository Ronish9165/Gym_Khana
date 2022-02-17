from django import forms
from django.contrib.auth import get_user_model
from product.models import Products, Booking



class ProductForm(forms.ModelForm): 
    class Meta:
        model = Products
        fields = ("__all__")

class BookForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = ("__all__")