from django.contrib import admin
from django.utils.html import format_html

from .models import Good, GoodImage, Subcategory, Category, Brand


@admin.register(GoodImage)
class GoodImageAdmin(admin.ModelAdmin):
    list_display = ("id", "good", "image")


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Main data", {"fields": ("id", "title", "slug")}
        ),
        (
            "Price", {"fields": ("price", "discount")}
        ),
        (
            "Info", {"fields": ("description", "brand", "made_in_country", "photo", "amount")}
        ),
    )

    def photo_image(self, obj):
        return format_html('<img style="width:100%" src="{}" />'.format(obj.photo.url))

    photo_image.short_description = 'Image'

    list_display = ("id", "photo_image", "title", "total_price",)
    list_display_links = ("id", "photo_image", 'title')
    list_filter = ("title", )
    readonly_fields = ("slug", "id")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")
    list_filter = ("country", "name")
