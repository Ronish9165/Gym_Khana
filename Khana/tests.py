from django.urls import reverse,resolve
from django.test import TestCase
from django.test import Client, SimpleTestCase, TestCase
from Khana.views import home, register,login, contact ,about, logout,edit_profile_view,profile,showblog

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_home_url(self):
        url=reverse("home")
        print(resolve(url))
        self.assertEquals(resolve(url).func,home)

    def test_case_register_url(self):
        url=reverse("register")
        print(resolve(url))
        self.assertEquals(resolve(url).func,register)

    def test_case_login_url(self):
        url=reverse("login")
        print(resolve(url))
        self.assertEquals(resolve(url).func,login)

    def test_case_contact_url(self):
        url=reverse("contact")
        print(resolve(url))
        self.assertEquals(resolve(url).func,contact)

    def test_case_about_url(self):
        url=reverse("about")
        print(resolve(url))
        self.assertEquals(resolve(url).func,about)

    def test_case_logout_url(self):
        url=reverse("logout")
        print(resolve(url))
        self.assertEquals(resolve(url).func,logout)

    
    def test_case_profile_url(self):
        url=reverse("profile")
        print(resolve(url))
        self.assertEquals(resolve(url).func,profile)

    def test_case_edit_profile_view_url(self):
        url=reverse("edit-profile")
        print(resolve(url))
        self.assertEquals(resolve(url).func,edit_profile_view)

    def test_case_blog_url(self):
         url=reverse("blog")
         print(resolve(url))
         self.assertEquals(resolve(url).func,showblog)


class Testviews(TestCase):
    def test_views_index(self):
        client=Client()
        url=reverse('Khana:home')
        response=client.post(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"homepage.html")



    def test_views_indbhex(self):
        client=Client()
        url=reverse('Khana:home')
        response=client.post(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"hommee.html")
