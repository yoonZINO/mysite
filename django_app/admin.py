from django.contrib import admin
from django_app.models import contact


@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email', 'created_date', 'updated_date']
    list_filter = ['name', 'email', 'created_date']
    search_fields = ['subject', 'message']