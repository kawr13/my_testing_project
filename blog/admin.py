from django.contrib import admin

from blog.models import Posts
from django.utils.html import mark_safe

# Register your models here.


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'preview', 'display_image', 'created_at')
    search_fields = ('title',)
    list_filter = ('title',)
    list_editable = ('description', 'preview')
    readonly_fields = ('created_at',)

    def display_image(self, obj):
        # Здесь вы можете создать HTML-код для отображения изображения
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        else:
            return 'Нет изображения'

    display_image.short_description = 'Изображение'
