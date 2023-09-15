from django.contrib import admin

from .models import Category, New


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'created_at', 'author', 'is_published',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'description', 'is_published',
    list_filter = 'category', 'author', 'is_published',
    list_per_page = 15
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',)
    }


admin.site.register(Category, CategoryAdmin)
