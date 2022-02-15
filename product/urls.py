from django.contrib import admin
from django.urls import path
from product import views


urlpatterns = [
    path('form', views.productform, name="form"),
    path('product', views.showproduct, name="product"),

     path('<int:id>', views.product_detail, name='product_detail'),
]