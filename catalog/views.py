from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Products


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method != "POST":
        return render(request, 'contacts.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"{name}, благодарим Вас за обращение!")
    return render(request,'contacts.html')


def products_list(request):
    products = Products.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)


def products_details(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {"product": product}
    return render(request, 'products_details.html', context)
