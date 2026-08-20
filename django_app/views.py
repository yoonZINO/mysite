from django.shortcuts import render
from django.http import HttpResponse

def Home_view(requests):
    return HttpResponse('this is home page')

def About_view(requests):
    return HttpResponse('this iS about page')

def Contact_view(requests):
    return HttpResponse('this is Contact page')
