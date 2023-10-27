from django.urls import path, re_path
from . import views

app_name = "weblog"

urlpatterns = [
    path("list", views.WeblogListView.as_view(), name="all_weblogs"),
    re_path(r'(?P<slug>[-\w]+)', views.WeblogDetailView.as_view(), name="weblog_detail"),
]
