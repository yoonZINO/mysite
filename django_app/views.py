from django.shortcuts import render
from django_app.forms import contactform
from django.http import HttpResponse

def Home_view(requests):
    return render(requests, 'django_app\\index.html')

def About_view(requests):
    return render(requests, 'django_app\\about.html')

def Contact_view(requests):
    return render(requests, 'django_app\\contact.html')

def testblog(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
             
        else:
            return HttpResponse('isnt valid')
    form = contactform()    
    return render(request, 'test.html', {'form': form})
