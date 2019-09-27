from django.contrib import admin

# Register your models here.
from .models import Article, Reporter

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')

class ReporterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Reporter, ReporterAdmin)