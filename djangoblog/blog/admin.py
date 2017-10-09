from django.contrib import admin
from .models import Blog,Category,Tag
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'body', 'created_time', 'modified_time', 'category']
    list_filter = ['category', 'tag', 'author']
    search_fields = ['category__name', 'tag__name', 'author']
admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category,CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Tag,TagAdmin)