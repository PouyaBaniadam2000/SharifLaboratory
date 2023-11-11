from django.urls import path, re_path
from . import views

app_name = "laboratory"

urlpatterns = [
    path("list", views.LaboratoryListView.as_view(), name="all_laboratories"),
    path('<str:slug>', views.LaboratoryDetailView.as_view(), name="laboratory_detail"),
    path('category/<str:slug>', views.CategoryDetailView.as_view(), name='category_laboratories'),
]
