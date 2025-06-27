from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.form import ProductForm, ProductModeratorForm
from catalog.models import Products, Category
from catalog.services import get_products_cache, get_products_by_category


class HomeView(TemplateView):
    template_name = "home.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"


class ProductListView(ListView):
    model = Products
    template_name = 'products_list.html'

    def get_queryset(self):
        return get_products_cache()



class ProductDetailView(DetailView):
    model = Products
    template_name = 'products_details.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # увеличиваем счетчик просмотров при каждом просмотре
        obj.views_counter += 1
        obj.save(update_fields=['views_counter'])
        return obj


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')
    template_name = 'product_form.html'

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')
    template_name = 'product_form.html'

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("products.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Products
    success_url = reverse_lazy('products:products_list')
    template_name = 'product_del_conf.html'


class ProductsByCategoryDetailView(DetailView):
    model = Category
    template_name = 'category_products.html'
    context_object_name = 'product_by_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_id = self.kwargs.get('pk')
        context["category_products"] = get_products_by_category(cat_id)
        return context

    def get_queryset(self):
        queryset = cache.get('my_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('my_queryset', queryset, 60 * 15)  # Кешируем данные на 15 минут
        return queryset

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'