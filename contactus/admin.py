from contactus.models import Message, ContactInfo, Complaint
from django.contrib import admin


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'mobile_phone', 'email', 'body')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        'work_time', 'email', 'mobile_phone', 'telegram', 'whatsapp', 'eitta', 'landline_phone_1',
        'landline_phone_2', 'address')
    list_editable = (
        'email', 'mobile_phone', 'telegram', 'whatsapp', 'eitta', 'landline_phone_1', 'landline_phone_2')


@admin.register(Complaint)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ("user", "body")
