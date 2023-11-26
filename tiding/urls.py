from django.urls import path, re_path
from . import views

app_name = "tiding"

urlpatterns = [
    path("list", views.TidingListView.as_view(), name="all_tidings"),
    path('<slug>', views.TidingDetailView.as_view(), name="tiding_detail"),

]
