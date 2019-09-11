from django.contrib import admin

# Register your models here.
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job')

admin.site.register(Job, JobAdmin)