from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView


app_name = CatalogConfig.name


urlpatterns = [

    path('', ProductListView.as_view(), name='products_list'),
    path('products_details/<int:pk>/', ProductDetailView.as_view(), name='products_details'),
    path('products_create/', ProductCreateView.as_view(), name='products_create'),
    path('<int:pk>/products_update/', ProductUpdateView.as_view(), name='products_update'),
    path('<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),
]