from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django_app.forms import contactform

def Home_view(requests):
    return render(requests, 'django_app\\index.html')

def About_view(requests):
    return render(requests, 'django_app\\about.html')

def Contact_view(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = contactform()

    return render(request, 'django_app\\contact.html', {'form': form})

def testblog(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
    form = contactform()    
    return render(request, 'test.html', {'form': form})
