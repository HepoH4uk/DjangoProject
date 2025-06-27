from django.core.cache import cache

from catalog.models import Products
from config.settings import CACHE_ENABLED


def get_products_cache():
    if not CACHE_ENABLED:
        return Products.objects.all()
    products_key = "products_list"
    products = cache.get(products_key)
    if products is not None:
        return products
    products = Products.objects.all()
    cache.set(products_key, products)
    return products


def get_products_by_category(category_pk):
    """Возвращает все продукты указанной категории"""
    return Products.objects.filter(category__pk=category_pk)


