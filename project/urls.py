from django.urls import path, re_path
from . import views

app_name = "project"

urlpatterns = [
    path("list", views.ProjectListView.as_view(), name="all_projects"),
    re_path(r'(?P<slug>[-\w]+)', views.ProjectDetailView.as_view(), name="project_detail"),

]
