from django.urls import path
from . import views


app_name = 'user_account' #assign app name to detemine for buttons in site when click them and move to baid page
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup')
]