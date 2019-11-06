from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import category

from .models import Item

from datetime import datetime

def index(request):
  items = Item.objects.order_by('-date_listed').filter(is_published=True)

  paginator = Paginator(items, 6)
  page = request.GET.get('page')
  paged_items = paginator.get_page(page)
  
  context = {
    'items': paged_items,
  }
  return render(request, 'items/items.html', context)

def item(request, item_id):
  item = get_object_or_404(Item, pk=item_id)

  context = {
    'item': item
  }

  return render(request, 'items/item.html', context)

def search(request):
  queryset_list = Item.objects.order_by('-date_listed')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(title__icontains=keywords) | queryset_list.filter(description__icontains=keywords)

  # elif 'category' in request.GET:
  #   category = request.GET['category_list']
  #   if category:
  #     queryset_list = queryset_list.filter(category__iexact=category)

  context = {
    'category': Item.category_list,
    'items': queryset_list,
    'values': request.GET
  }

  return render(request, 'items/search.html', context)
