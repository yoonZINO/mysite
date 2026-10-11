from django.contrib import admin
from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): #name of class-> [name of model][changing admin]
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ['title','author', 'counted_view', 'status', 'created_date', 'updated_date']
    list_filter = ['status', 'created_date', 'counted_view', 'author']
    search_fields = ['title', 'content']
