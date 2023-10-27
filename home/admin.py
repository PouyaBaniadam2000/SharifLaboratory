from django.contrib import admin
from home.models import GeneralWebsiteIdea, GeneralWebsiteIdeaImage, SharifLabServicePreview, TeamMember, Certificate


@admin.register(GeneralWebsiteIdea)
class GeneralWebsiteIdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')


@admin.register(GeneralWebsiteIdeaImage)
class GeneralWebsiteIdeaImageAdmin(admin.ModelAdmin):
    list_display = ('display_image',)

    def display_image(self, obj):
        return obj.show_image()

    display_image.short_description = 'تصویر'


@admin.register(SharifLabServicePreview)
class SharifLabServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'about', 'display_image')

    def display_image(self, obj):
        return obj.show_image()

    display_image.short_description = 'تصویر'


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image')

    def display_image(self, obj):
        return obj.show_image()

    display_image.short_description = 'تصویر'
