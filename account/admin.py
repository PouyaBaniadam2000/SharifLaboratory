from account.models import CustomUser, OTP
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = (
        'mobile_phone', 'username', 'first_name', 'last_name', 'landline_phone', 'postal_code', 'address',
        'company_name', 'activity_field', 'display_image', 'is_staff', 'is_superuser')

    search_fields = (
        'mobile_phone', 'username', 'first_name', 'last_name', 'landline_phone', 'postal_code', 'company_name',
        'activity_field', 'email')
    readonly_fields = ('date_joined',)
    list_filter = ('is_staff',)
    list_per_page = 50
    ordering = ('-date_joined',)
    search_help_text = ('جستجو بر اساس شماره تلفن همراه و ثابت، کد پستی، نام شرکت، حوزه فعالیت، نام کاربری، نام، نام '
                        'خانوادگی و آدرس ایمیل امکان پذیر است.')

    list_editable = ()
    filter_horizontal = ()
    fieldsets = ()

    def display_image(self, obj):
        return obj.show_image()

    display_image.short_description = 'تصویر پروفایل'


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(OTP)
