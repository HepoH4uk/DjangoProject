from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
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


class ProductCreateView(CreateView):
    model = Products
    fields = ("name","description","image","category","purchase_price")
    success_url = reverse_lazy('products:products_list')
    template_name = 'product_form.html'


class ProductUpdateView(UpdateView):
    model = Products
    fields = ("name","description","image","category","purchase_price")
    success_url = reverse_lazy('products:products_list')
    template_name = 'product_form.html'


class ProductDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('products:products_list')
    template_name = 'product_del_conf.html'