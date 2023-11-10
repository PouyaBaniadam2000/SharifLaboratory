from django.contrib import admin
from laboratory.models import Laboratory, Category


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = (
        "title", "laboratory_preview", "display_image_1", "display_image_2", "display_image_3", "display_image_4",
        "is_allowed", "created_at")
    list_editable = ("is_allowed",)
    prepopulated_fields = {"slug": ["title"]}

    def display_image_1(self, obj):
        return obj.show_image_1()

    display_image_1.short_description = 'تصویر آزمایشگاه 1'

    def display_image_2(self, obj):
        return obj.show_image_2()

    display_image_2.short_description = 'تصویر آزمایشگاه 2'

    def display_image_3(self, obj):
        return obj.show_image_3()

    display_image_3.short_description = 'تصویر آزمایشگاه 3'

    def display_image_4(self, obj):
        return obj.show_image_4()

    display_image_4.short_description = 'تصویر آزمایشگاه 4'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "parent", "slug")
    prepopulated_fields = {"slug": ["title"]}
