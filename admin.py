from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')  # Fields to display in the admin panel
    search_fields = ('name', 'email', 'message')  # Fields to search within the admin panel
