from django.shortcuts import render, redirect, get_object_or_404
from .models import Item


def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'items/item_list.html', context)