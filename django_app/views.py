from django.shortcuts import render, get_object_or_404

def Home_view(requests):
    return render(requests, 'website\\index.html')

def About_view(requests):
    return render(requests, 'website\\about.html')

def Contact_view(requests):
    return render(requests, 'website\\contact.html')
