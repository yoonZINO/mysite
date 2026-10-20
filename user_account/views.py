from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.user.authenticated:
        msg = f"you are loged in as {request.user.username}"
    else:
        msg = "loging in fails"
    return render(request, 'user_account/login.html', {'msg': msg})

#def logout_view(request):
#    pass

#def signup_view(request):
 #   return render(request, 'user_account./signup.html')