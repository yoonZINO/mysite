from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_view(requests, Author_username=None):
    Posts = Post.objects.filter(status=1)
    if Author_username:
        Posts = Posts.filter(author__username = Author_username)
    context = {'posts': Posts}
    return render(requests, 'blog\\blog-home.html', context)

def blog_single(requests, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post':post}
    return render(requests, 'blog\\blog-single.html', context)

def testblog(requests):
    return render(requests, 'test.html')

