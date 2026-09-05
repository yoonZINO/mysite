from django.urls import path
from . import views
from django_app.views import Home_view, About_view, Contact_view


app_name = 'blog' #assign app name to detemine for buttons in site when click them and move to baid page
urlpatterns = [
    path('',views.blog_view, name='index'), #for blog/index
    path('blog-home.html/', views.blog_view, name='indexblog'),
    path('index.html/', Home_view, name='index_blog'),
    path('about.html/', About_view, name='about_blog'),
    path('contact.html/', Contact_view, name='contact_blog'),
    path('blog-single/', views.blog_single, name='single'), #for blog/single
    path('blog-single/index.html/', Home_view, name='index_single_blog'),
    path('blog-single/about.html/', About_view, name='about_single_blog'),
    path('/blog-single/contact.html/', Contact_view, name='contact_single_blog'),
]