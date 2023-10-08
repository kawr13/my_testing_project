from django.contrib import admin
from portfolio.models import Projects
from django.utils.html import mark_safe



@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'display_image', 'url_address')
    search_fields = ('title',)
    list_filter = ('title',)
    list_editable = ('description', 'url_address')

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        else:
            return 'Нет изображения'

    display_image.short_description = 'Изображение'