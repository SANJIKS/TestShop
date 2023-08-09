from django.urls import path
from .views import ProductView, ExportProductsView

urlpatterns = [
    path('api/products/', ProductView.as_view()),
    path('api/products/export/', ExportProductsView.as_view(), name='export-products'),
]