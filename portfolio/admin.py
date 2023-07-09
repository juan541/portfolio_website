from django.contrib import admin
from .models import Projects, Contact
# Register your models here.
admin.site.register(Projects)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')