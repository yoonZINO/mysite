from django.contrib import admin
from blog.models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(admin.ModelAdmin): #name of class-> [name of model][changing admin]
    pass

class sumernote(SummernoteModelAdmin):
    pass


class main(PostAdmin, sumernote):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ['title','author', 'counted_view', 'status', 'created_date', 'updated_date']
    list_filter = ['status', 'created_date', 'counted_view', 'author']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Post, main)




    
