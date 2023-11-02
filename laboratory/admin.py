from django.contrib import admin
from laboratory.models import Category, Laboratory


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Category)
