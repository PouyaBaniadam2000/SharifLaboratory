from django.urls import path
from . import views

app_name = "about"

urlpatterns = [
    path("about-us", views.AboutUsView.as_view(), name="about_us"),
    path("faq", views.FaqView.as_view(), name="faq"),

]