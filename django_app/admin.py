from django.contrib import admin
from django_app.models import contact
# Register your models here.

class contctadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['subject', 'email', 'created_date', 'updated_date']
    list_filter = ['name', 'email', 'created_date']
    search_fields = ['sunject', 'message']

admin.site.register(contact, contctadmin)