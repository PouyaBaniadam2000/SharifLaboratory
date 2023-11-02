from django.urls import path, re_path
from . import views

app_name = "product"

urlpatterns = [
    path("products", views.AllLaboratory.as_view(), name="all_products"),
    re_path(r'products/(?P<slug>[-\w]+)', views.LaboratoryDetail.as_view(), name="product_detail"),
    path('category/<int:category_id>/', views.CategoryLaboratoryListView.as_view(), name='category_products'),

]