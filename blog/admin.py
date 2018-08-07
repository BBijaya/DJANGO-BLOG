from django.contrib import admin
from .models import Post ,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """ defining post view in admin """
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status','publish']
admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    """ defining comment view in admin """
    list_display = ('name','email','post','created','active')
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')
admin.site.register(Comment, CommentAdmin)
