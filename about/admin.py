from about.models import About, Faq
from django.contrib import admin


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
