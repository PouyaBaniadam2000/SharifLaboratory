from django.contrib import admin
from weblog.models import Weblog, Category


@admin.register(Weblog)
class WeblogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'weblog_preview', 'is_allowed', 'actual_jalali_date')
    list_editable = ('is_allowed',)
    prepopulated_fields = {"slug": ["title"]}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
