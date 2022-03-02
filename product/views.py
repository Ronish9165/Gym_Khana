from django.shortcuts import render,redirect
from product.forms import ProductForm, BookForm
from product.models import Products, Booking
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator

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

# @login_required(login_url='login')
# def product_detail(request, id):
#     single_product = get_object_or_404(Products, pk=id)

#     data = {
#         'single_product': single_product,
#     }

#     return render(request, 'product/product_detail.html', data)
@login_required(login_url='login')
def purchase(request, p_id):
    print(request)
    if request.method == "POST":
        form = BookForm(request.POST)
        print(request)
        try:
            form.save()
            messages.success(request, "your booking was done")
            return redirect('/')
        except:
            print("error")
    else:
        form = BookForm()
    products = Products.objects.get(product_id=p_id)
    return render(request, 'product/purchase.html', {'products': products, 'form': form})


@login_required(login_url='login')
def book_details(request, p_id):
    purchase = Products.objects.get(product_id=p_id)
    return render(request, 'admin/purchase.html', {'Products': purchase})

@login_required(login_url='login')
def admindashboard_view(request):
    user = get_user_model()
    usercount = user.objects.all().filter(is_superuser=False).count()
    productcount = Products.objects.all().count()
    # productcount = Khana.objects.all().count()
    
    order = Products.objects.all()
    data = {
        'order': order,
        'usercount':usercount,
        # 'bookingcount':bookingcount,
        'productcount':productcount,
    }
    if request.user.is_superuser:
        user = User.objects.all()
        return render(request, 'adminControl/admindashboard.html', data)
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('admin')


@login_required(login_url='adminlogin')
def view_product(request):
    user = get_user_model()
    product=Products.objects.all()
    usercount = user.objects.all().filter(is_superuser=False).count()
    productcount = Products.objects.all().count()
    bookingcount = Booking.objects.all().count()
    data = {
        'product':product,
        'usercount':usercount,
        'bookingcount':bookingcount,
        'productcount':productcount,
        
    }
    return render(request,'admin/view_product.html',data)


@login_required(login_url='adminlogin')
def view_booking(request):
    user = get_user_model()
    booking=Booking.objects.all()
    usercount = user.objects.all().filter(is_superuser=False).count()
    bookingcount = Booking.objects.all().count()
    productcount = Products.objects.all().count()
    product = Products.objects.all()
    data = {
        'booking':booking,
        'usercount':usercount,
        'bookingcount':bookingcount,
        'productcount':productcount,
        'products':product
        
    }
    return render(request,'admin/view_booking.html',data)

@login_required(login_url='login')  
def edit_product(request,p_id):

    try:

       product=Products.objects.get(product_id=p_id)

       return render(request, "product/product_edit.html", {'product':product})

    except:

       print("No Data Found")

    return redirect("/product/viewproduct")

@login_required(login_url='login')
def update_product(request,p_id):

    product=Products.objects.get(product_id=p_id)

    form=ProductForm(request.POST, instance=product)

    form.save()

    return redirect ("/product/view-product")

@login_required(login_url='login')
def delete_product(request, p_id):
    product = Products.objects.get(product_id=p_id)
    product.delete()
    return redirect('/product/view-product')