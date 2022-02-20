from django.contrib import admin
from django.urls import path
from Khana import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path("login/", views.login, name='login'),
    # path("login_fn", views.login_fn, name='login_fn'),
    path("register/", views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('blogform', views.blogform, name="blogform"),
    path('blog', views.showblog, name='blog'),
    path('view-blog', views.view_blog, name='view-blog'),
    path('<int:id>', views.blog_detail, name='blog_detail'),
    path('logout', views.logout, name="logout"),
    path('adminlogin',LoginView.as_view(template_name='admin/adminlogin.html'), name="adminlogin"),
    path('profile', views.profile, name='profile'),
    path('deleteuser/<int:user_id>', views.delete_user, name='delete_user'),
    path('admindashboard', views.admin_dashboard_view, name='admindashboard'),
    path('view-customer', views.view_customer, name='view-customer'),

    path('edit_blog/<int:p_id>', views.edit_blog,name='edit_blog'),
    path('update_blog/<int:p_id>', views.update_blog,name='update_blog'),
    path('delete_blog/<int:p_id>', views.delete_blog,name='delete_blog'),
   

    # path("homepage/",views.homepage, name='homepage'),

    
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset_form.html'),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'),
         name='password_reset_complete'),

     # User Related Views
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
]
