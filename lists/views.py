from django.http import HttpResponse
from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    """Домашняя страница"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/first-list/')
    items = Item.objects.all()
    return render(request, 'home.html')


def view_list(request):
    """Представление списка"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

