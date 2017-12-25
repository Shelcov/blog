from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]
    list_filter = ['tag', 'is_active', 'user']
    search_fields = ['name']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]
    search_fields = ['name']

    class Meta:
        model = Tag


admin.site.register(Tag, TagAdmin)
