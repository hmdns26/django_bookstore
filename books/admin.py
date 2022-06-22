from django.contrib import admin
from .models import Book, Comment
# Register your models here.


admin.site.register(Book)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_created',)


admin.site.register(Comment, CommentAdmin)
