from django.contrib import admin
from blog.models import Post, Category

# Register your models here.
class Postadmin(admin.ModelAdmin): #name of class-> [name of model][changing admin]
    date_hierarchy ='created_date'
    empty_value_display = "-empty-"
    list_display = ['title','author', 'counted_view', 'status', 'created_date', 'updated_date']
    list_filter = ['status', 'created_date', 'counted_view', 'author']
    search_fields = ['title', 'content']

admin.site.register(Category)
admin.site.register(Post, Postadmin) #registering model to be shown in admin page
