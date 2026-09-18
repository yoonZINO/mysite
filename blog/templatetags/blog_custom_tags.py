from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag(name="post_counter")
def func():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name="posts")
def func():
    posts = Post.objects.filter(status=1)
    return posts

@register.inclusion_tag('blog/blog-latesst-post.html')
def latestpost():
    posts = Post.objects.filter(status=1).order_by('created_date')
    return {'posts': posts}