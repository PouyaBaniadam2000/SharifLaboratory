from django.contrib import admin
from laboratory.models import Laboratory, Category


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = (
        "title", "laboratory_preview", "display_image_1","is_allowed", "created_at")
    list_editable = ("is_allowed",)
    prepopulated_fields = {"slug": ["title"]}

    def display_image_1(self, obj):
        return obj.show_image_1()

    display_image_1.short_description = 'تصویر آزمایشگاه 1'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "parent", "slug")
    prepopulated_fields = {"slug": ["title"]}
