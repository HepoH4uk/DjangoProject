from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method != "POST":
        return render(request, 'contacts.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"{name}, благодарим Вас за обращение!")
    return render(request,'catalog/templates/contacts.html')