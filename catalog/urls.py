from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView, CatalogCreateView, CatalogUpdateView, CatalogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='catalog_list'),
    path('catalog/<int:pk>/', CatalogDetailView.as_view(), name='catalog_detail'),
    path('catalog/create', CatalogCreateView.as_view(), name='catalog_create'),
    path('catalog/<int:pk>/update', CatalogUpdateView.as_view(), name='catalog_update'),
    path('catalog/<int:pk>/delete', CatalogDeleteView.as_view(), name='catalog_delete')
]
