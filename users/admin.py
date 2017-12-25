from django.contrib import admin
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    list_filter = ['user', 'post', 'created']

    class Meta:
        model = Comment
    

admin.site.register(Comment, CommentAdmin)
