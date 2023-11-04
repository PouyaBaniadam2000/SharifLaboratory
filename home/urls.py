from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.Home.as_view(template_name="home/index.html"), name="home"),
    path('search/', views.search_view, name='search_view'),

]
