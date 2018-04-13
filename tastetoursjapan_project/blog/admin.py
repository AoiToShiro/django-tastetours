
from django.contrib import admin

# Register your models here.
from .models import Post
from mediumeditor.admin import MediumEditorAdmin

class PostAdmin(MediumEditorAdmin, admin.ModelAdmin):
    list_display = ('title','slug','author','status','created')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    mediumeditor_fields = ('body')

admin.site.register(Post, PostAdmin)
