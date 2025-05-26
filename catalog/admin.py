from django.contrib import admin
from catalog.models import Products, Category


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "purchase_price")
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", "description",)
