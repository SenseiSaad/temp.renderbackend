from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'received_at', 'is_read')
    list_editable = ('is_read',)
    list_filter = ('is_read', 'received_at')

admin.site.register(Contact, ContactAdmin)
