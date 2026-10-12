from django.shortcuts import render
from django.contrib import messages
from django_app.forms import contactform

def Home_view(requests):
    return render(requests, 'django_app\\index.html')

def About_view(requests):
    return render(requests, 'django_app\\about.html')

def Contact_view(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        print (request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "your ticket submited")
        else:
            print(form.errors)
            messages.add_message(request, messages.ERROR, "error while submiting ticket")

    form = contactform()

    return render(
        request,
        'django_app/contact.html',
        {'form': form}
    )




#def testblog(request):
 #   if request.method == 'POST':
  #      form = contactform(request.POST)
   #     if form.is_valid():
    #        form.save()
    #form = contactform()    
    #return render(request, 'test.html', {'form': form})