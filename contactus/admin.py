from contactus.models import Message, ContactInfo, Complaint
from django.contrib import admin


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'mobile_phone', 'email', 'body')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'work_time', 'email', 'mobile_phone', 'landline_phone')
    list_editable = ('email', 'work_time', 'mobile_phone', 'landline_phone')


@admin.register(Complaint)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ("user", "body")