from django.contrib import admin
from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'subcategory')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
