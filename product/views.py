from django.shortcuts import render,redirect
from product.forms import ProductForm
from product.models import Products

# Create your views here.

def productform(request):

    print(request.FILES)

    if request.method=="POST":

        products=ProductForm(request.POST,request.FILES)

        products.save()
        return redirect ("/product/product")

       



    else:

        products=ProductForm()

     

    return render (request,"product/product_form.html",{'products':products})


def showproduct(request):
    products=Products.objects.all()
    return render (request,"product/product.html",{'products':products})
