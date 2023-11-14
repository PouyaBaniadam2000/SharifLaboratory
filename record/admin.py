from django.contrib import admin
from record.models import Record, Category


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'record_preview', 'display_image', 'is_allowed')
    list_editable = ('is_allowed',)
    prepopulated_fields = {"slug": ["title"]}

    def display_image(self, obj):
        return obj.show_image()

    display_image.short_description = 'تصویر'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
