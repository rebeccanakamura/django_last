from django.shortcuts import render
from django.http import HttpResponse
from items.choices import category

from items.models import Item
from sellers.models import Seller

def index(request):
    items = Item.objects.order_by('-date_listed').filter(is_published=True)[:6]

    context = {
        'items': items,
        'category': Item.item.category,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    sellers = Seller.objects.order_by('-date_joined')

    context = {
        'sellers': sellers
    }
    return render(request, 'pages/about.html', context)
