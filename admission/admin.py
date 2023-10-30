from django.contrib import admin

from admission.models import Admission


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = (
        "company_name", "national_code", "address", "landline_phone", "mobile_phone", "email", "request_date",
        "instance_sent_date", "test_name", "instance_details", "description",)
