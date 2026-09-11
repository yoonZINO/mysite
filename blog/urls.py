from django.urls import path
from . import views


app_name = 'blog' #assign app name to detemine for buttons in site when click them and move to baid page
urlpatterns = [
    path('',views.blog_view, name='index'), #for blog/index
    path('single', views.blog_single, name='single'),
 #   path('testblog', views.testblog, name='testblog')
]