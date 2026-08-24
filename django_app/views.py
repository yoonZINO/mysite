from django.shortcuts import render

def Home_view(requests):
    return render(requests, 'website\\home.html')

def About_view(requests):
    return render(requests, 'website\\about.html')

def Contact_view(requests):
    return render(requests, 'website\\contact.html')
