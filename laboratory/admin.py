from django.contrib import admin
from laboratory.models import Laboratory, Category


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Category)
