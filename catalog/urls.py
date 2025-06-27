from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView, ProductsByCategoryDetailView

app_name = CatalogConfig.name


urlpatterns = [

    path('', ProductListView.as_view(), name='products_list'),
    path('products_details/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_details'),
    path('products_create/', ProductCreateView.as_view(), name='products_create'),
    path('<int:pk>/products_update/', ProductUpdateView.as_view(), name='products_update'),
    path('<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/category/<int:pk>', ProductsByCategoryDetailView.as_view(), name='products_category'),
    path('product/category/', CategoryListView.as_view(), name='category_list'),
]