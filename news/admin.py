from django.contrib import admin

from .models import Category, New


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    ...
