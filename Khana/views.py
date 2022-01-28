from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import  authenticate
from django.contrib.auth.models import auth, User
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'pages/homepage.html')
 
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:  
        return render(request, 'pages/login.html')   


def register(request):

    if request.method =='POST':
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

    if request.method == 'POST':

        auth.logout(request)

        # messages.success(request, 'You are successfully logged out.')

        return redirect('login')

    return redirect('home')