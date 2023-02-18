from django.contrib import admin

from images.models import Img, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('author', 'text', 'date', 'img')
    list_display = ('author', 'date', 'img')
    readonly_fields = ('date', )
    list_filter = ('date', )
    search_fields = ('author', 'text')
   