from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def blog_view(requests, Author_username=None):
    Posts = Post.objects.filter(status=1)
    if Author_username:
        Posts = Posts.filter(author__username = Author_username)
    Posts = Paginator(Posts, 4)
    page_numb = requests.GET.get('page')
    try:
        Posts = Posts.get_page(page_numb)
    except PageNotAnInteger:
        Posts = Posts.page(1)
    except EmptyPage:
        Posts = Posts.page(Posts.num_pages)
    context = {'posts': Posts}
    return render(requests, 'blog\\blog-home.html', context)

def blog_single(requests, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post':post}
    return render(requests, 'blog\\blog-single.html', context)

def blog_search(request):
    Posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if request.GET.get('s'):
            Posts = Posts.filter(content__contains = request.GET.get('s'))
    context = {'posts': Posts}
    return render(request, 'blog\\blog-home.html', context)

def testblog(requests):
    return render(requests, 'test.html')

