from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category

def blog_view(requests):
    Posts = Post.objects.filter(status=1)
    context = {'posts': Posts}
    return render(requests, 'blog\\blog-home.html', context)

def blog_single(requests, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post':post}
    return render(requests, 'blog\\blog-single.html', context)

def testblog(requests):
    return render(requests, 'test.html')

