from django.urls import path, re_path
from . import views

app_name = "record"

urlpatterns = [
    path("list", views.RecordListView.as_view(), name="all_records"),
    re_path(r'(?P<slug>[-\w]+)', views.RecordDetailView.as_view(), name="record_detail"),

]
