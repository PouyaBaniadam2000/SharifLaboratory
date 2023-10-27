from contactus.models import Message, ContactInfo
from django.contrib import admin


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'mobile_phone', 'email', 'body')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'mobile_phone', 'landline_phone')
    list_editable = ('email', 'mobile_phone', 'landline_phone')
