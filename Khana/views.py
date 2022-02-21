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
            messages.info(request, 'Incorrect Username or password.')
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
    usercount = User.objects.all().filter(is_superuser=False).count()
    bookingcount = Booking.objects.all().count()
    productcount = Products.objects.all().count()

    data={
            'usercount':usercount,
            'bookingcount':bookingcount,
            'productcount':productcount,
        
            
        }


 

    if request.method=="POST":

        blogs=BlogForm(request.POST,request.FILES)
        
       

        blogs.save()
        return redirect ("blog")

    else:

        blogs=BlogForm()

     

    return render (request,"pages/blog_form.html",{'Khana':blogs})


def showblog(request):
    user = get_user_model()
    blogs=Blogs.objects.all()

    return render (request,"pages/blog.html",{'blogs':blogs,})

@login_required(login_url='login')
def blog_detail(request, id):
    single_blog = get_object_or_404(Blogs, pk=id)
    usercount = User.objects.all().filter(is_superuser=False).count()
    productcount = Products.objects.all().count()
    # productcount = Khana.objects.all().count()

    data = {
        'single_blog': single_blog,
        'product':productcount,
       
        'usercount':usercount,
        # 'bookingcount':bookingcount,
        'productcount':productcount,
    }

    return render(request, 'pages/blog_detail.html', data)

def edit_blog(request,p_id):

    try:

       blog=Blogs.objects.get(blog_id=p_id)

       return render(request, "pages/blog_edit.html", {'single_blog':blog})

    except:

       print("No Data Found")

    return redirect("/view-blog")

def update_blog(request,p_id):

    blog=Blogs.objects.get(blog_id=p_id)
    form=BlogForm(request.POST,request.FILES, instance=blog)
    form.save()

    return redirect ("/view-blog")

def delete_blog(request, p_id):
    blog = Blogs.objects.get(blog_id=p_id)
    blog.delete()
    return redirect('/view-blog')



@login_required(login_url='adminlogin')
def view_blog(request):
    user = get_user_model()
    single_blog=Blogs.objects.all()
    usercount = user.objects.all().filter(is_superuser=False).count()
    productcount = Products.objects.all().count()
    bookingcount = Booking.objects.all().count()
    data = {
        'single_blog':single_blog,
        'usercount':usercount,
        'bookingcount':bookingcount,
        'productcount':productcount,
        
    }
    return render(request,'admin/view_blog.html',data)

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

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'User is deleted successfully')
    return redirect('login')


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
    bookingcount = Booking.objects.all().count()
    
    order = Products.objects.all()
    data = {
        'order': order,
        'usercount':usercount,
        'bookingcount':bookingcount,
        'productcount':productcount,
    }
    return render(request, 'admin/admindashboard.html',data)

@login_required(login_url='adminlogin')
def view_customer(request):
    User = get_user_model()
    users=User.objects.all().order_by('username').filter(is_superuser=False)
    paginator = Paginator(users, 2)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    usercount = User.objects.all().filter(is_superuser=False).count()
    productcount = Products.objects.all().count()
    bookingcount = Booking.objects.all().count()
    data = {
        'users': paged_product,
        'usercount':usercount,
        'bookingcount':bookingcount,
        'productcount':productcount,
        
    }
    return render(request,'admin/view_customer.html',data)

