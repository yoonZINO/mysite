from django.urls import path
from . import views
from blog.rss_feed import LatestEntriesFeed



app_name = 'blog' #assign app name to detemine for buttons in site when click them and move to baid page
urlpatterns = [
    path('',views.blog_view, name='index'), #for blog/index
    path('blog/<int:pid>', views.blog_single, name='single'),
    path('Author/<str:Author_username>', views.blog_view, name='ListByAuthor'),
    path('Search/', views.blog_search, name='search'),
    path('tag/<str:tag_name>', views.blog_view, name='tag'),
    path("rss/feed/", LatestEntriesFeed()),

] 