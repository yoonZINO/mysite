from django.urls import path
from . import views
from django_app.views import Home_view, About_view, Contact_view


app_name = 'blog' #assign app name to detemine for buttons in site when click them and move to baid page
urlpatterns = [
    path('',views.blog_view, name='index'), #for blog/index
    path('index.html/', Home_view, name='index'),
    path('about.html/', About_view, name='about'),
    path('index.html/', Contact_view, name='contact'),
    path('single/', views.blog_single, name='single'), #for blog/single
    path('single/index.html', Home_view, name='index'),
    path('single/about.html', About_view, name='about'),
    path('single/contact.html', Contact_view, name='contact'),



]