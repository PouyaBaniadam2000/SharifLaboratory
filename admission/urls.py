from django.urls import path
from . import views

app_name = "admission"

urlpatterns = [
    path("form", views.AdmissionView.as_view(), name="form"),
]
