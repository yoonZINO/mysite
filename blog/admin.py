from django.contrib import admin
from blog.models import Post

# Register your models here.
class Postadmin(admin.ModelAdmin): #name of class-> [name of model][changing admin]
     date_hierarchy ='created_date'

admin.site.register(Post, Postadmin) #registering model to be shown in admin page