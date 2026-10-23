from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    return render(request, 'user_account/login.html')

#def logout_view(request):
#    pass

#def signup_view(request):
 #   return render(request, 'user_account./signup.html')