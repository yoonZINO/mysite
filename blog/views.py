from django.shortcuts import render
from blog.models import Post

def blog_view(requests):
    Posts = Post.objects.filter(status=1)
    context = {'posts': Posts}
    return render(requests, 'blog\\blog-home.html', context)

def blog_single(requests):
    return render(requests, 'blog\\blog-single.html')

#def testblog(requests):
  #  Posts = Post.objects.all()
 #   context = {'posts': Posts}
#    return render(requests, 'test.html', context)
