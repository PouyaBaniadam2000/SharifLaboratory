from django.contrib import admin
from tiding.models import Tiding, Category


@admin.register(Tiding)
class TidingAdmin(admin.ModelAdmin):
    list_display = ('title', 'tiding_preview', 'display_image', 'date', 'is_allowed')
    list_editable = ('is_allowed',)
    prepopulated_fields = {"slug": ["title"]}

    def display_image(self, obj):
        return obj.show_image()

    display_image.short_description = 'تصویر'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
