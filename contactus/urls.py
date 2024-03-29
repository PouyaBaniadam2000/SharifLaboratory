from django.urls import path
from . import views

app_name = "contact_us"

urlpatterns = [
    path("", views.ContactUsView.as_view(), name="contact_us"),
    path("complaint", views.ComplaintView.as_view(), name="complaint"),
]
