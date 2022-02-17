from django import forms
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import  authenticate,  get_user_model
from django.contrib.auth.models import auth, User
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from Khana.forms import UserResgistrationForm
from Khana.forms import BlogForm
from Khana.models import Blogs
from django.core.paginator import Paginator

from . import models
from product.models import *


User = get_user_model()

# Create your views here.

def home(request):
    return render(request, 'pages/homepage.html')
 
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if not user.is_staff:
                auth.login(request, user)
                return redirect('home')

            elif user.is_staff:
                auth.login(request, user)
                return redirect('admindashboard')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:  
        return render(request, 'pages/login.html')  



def register(request):
    form = UserResgistrationForm()
    if request.method =='POST':
        form = UserResgistrationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(
                            username=username,
                            email=email,
                            first_name=first_name,
                            password=password)
            user.save()
            print("here")
            return redirect('/login')
    else:
        return render(request, 'pages/register.html')
 

# def homepage(request):
#     return render(request, 'pages/homepage.html')

def about(request):
    return render(request, 'pages/aboutus.html')

def blogform(request):

    print(request.FILES)

    if request.method=="POST":

        blogs=BlogForm(request.POST,request.FILES)

        blogs.save()
        return redirect ("blog")

    else:

        blogs=BlogForm()

     

    return render (request,"pages/blog_form.html",{'Khana':blogs})


def showblog(request):
    blogs=Blogs.objects.all()
    return render (request,"pages/blog.html",{'blogs':blogs})

@login_required(login_url='login')
def blog_detail(request, id):
    single_blog = get_object_or_404(Blogs, pk=id)

    data = {
        'single_blog': single_blog,
    }

    return render(request, 'pages/blog_detail.html', data)

def contact(request):

    if request.method == "POST":

        message_name = request.POST['message_name']

        message_email = request.POST['message_email']

        message_subject = request.POST['message_subject']

        message =request.POST['message']



        send_mail(

            message_subject, #subject

            message, #message

            message_email, #from email

            ['sthronesh11@gmail.com' ], #To email

            # fail_silently= True,

        )  

        return render(request, 'pages/contactus.html', {'message_name': message_name})



    else:

        return render(request, 'pages/contactus.html' , {})      


def logout(request):
    auth.logout(request)
    # messages.success(request, "Sucessfully Logged Out")
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    return render(request, 'pages/profile.html')


@login_required(login_url='login')
def edit_profile_view(request):
    user=User.objects.get(id=request.user.id)
    userForm=UserResgistrationForm(instance=user)
    mydict={
        'UserResgistrationForm':UserResgistrationForm,
        'user':user
    }
    if request.method=='POST':
        userForm=UserResgistrationForm(request.POST, request.FILES, instance=user)
        if userForm.is_valid():
            user.set_password(user.password)
            userForm.save()
            # user.set_password(user.password)
            # user.save()
            return HttpResponseRedirect('profile')

    return render(request,'pages/edit_profile.html',context=mydict)
    
@login_required(login_url='login')
def admin_dashboard_view(request):
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
    return render(request, 'admin/admindashboard.html',data)

@login_required(login_url='adminlogin')
def view_customer(request):
    User = get_user_model()
    users=User.objects.all().order_by('username').filter(is_superuser=False)
    paginator = Paginator(users, 1)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'users': paged_product,
        
    }
    return render(request,'admin/view_customer.html',data)