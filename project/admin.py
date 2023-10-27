from django.contrib import admin
from project.models import Project, Category


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_preview', 'display_image', 'location', 'financial_value', 'date', 'is_allowed')
    list_editable = ('is_allowed',)
    prepopulated_fields = {"slug": ["title"]}

    def display_image(self, obj):
        return obj.show_image()

    display_image.short_description = 'تصویر'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
