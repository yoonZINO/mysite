from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('/')
    return render(request, 'user_account/login.html', {'form': form})
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                form = UserCreationForm()
        form = UserCreationForm()
        context = {'form': form}
    return render(request, 'user_account/signup.html', context)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'user_account/signup.html', {'form': form})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #if not request.user.is_authenticated:
   #     if request.method == 'POST':
      #      form = UserCreationForm(request.POST)
       #     if form.is_valid():
        #        form.save()
     #           return redirect('/')
     #       else:
      #          form = UserCreationForm() 
   #     form = UserCreationForm()
    #    context = {'form': form}
      #  return render(request, 'user_account/signup.html', context)
  #  else:
  #      return redirect('/')
    