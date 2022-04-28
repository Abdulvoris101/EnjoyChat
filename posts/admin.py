from django.contrib import admin
from .models import Post, Comment, Like, Verification


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author')
    list_display_links = ('id', 'author')

admin.site.register(Post, PostAdmin)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Like)

admin.site.register(Verification)