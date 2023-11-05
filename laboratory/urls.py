from django.urls import path, re_path
from . import views

app_name = "laboratory"

urlpatterns = [
    path("list", views.LaboratoryListView.as_view(), name="all_laboratories"),
    re_path(r'(?P<slug>[-\w]+)', views.LaboratoryDetailView.as_view(), name="laboratory_detail"),

]
