from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.form import ProductForm
from catalog.models import Products


class HomeView(TemplateView):
    template_name = "home.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"


class ProductListView(ListView):
    model = Products
    template_name = 'products_list.html'


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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')
    template_name = 'product_form.html'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Products
    success_url = reverse_lazy('products:products_list')
    template_name = 'product_del_conf.html'