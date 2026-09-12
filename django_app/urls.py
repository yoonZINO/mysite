from django.urls import path
from . import views


app_name = 'django_app' #assign app name to detemine for buttons in site when click them and move to baid page
urlpatterns = [
    path('',views.Home_view, name='index'),
    path('about/', views.About_view, name='about'),
    path('contact/', views.Contact_view, name='contact')
    
]