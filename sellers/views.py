from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Seller

def index(request):
  sellers = Seller.objects.order_by('-seller_date').filter(is_published=True)

  paginator = Paginator(items, 6)
  page = request.GET.get('page')
  paged_sellers = paginator.get_page(page)

  context = {
    'sellers': paged_sellers
  }

  return render(request, 'sellers/sellers.html', context)

def seller(request, item_id):
  seller = get_object_or_404(Seller, pk=seller_id)

  context = {
    'seller': seller
  }

  return render(request, 'sellers/seller.html', context)

# def search(request):
#   queryset_list = Seller.objects.order_by('-seller_date')

#   # Keywords
#   if 'keywords' in request.GET:
#     keywords = request.GET['keywords']
#     if keywords:
#       queryset_list = queryset_list.filter(description__icontains=keywords)

#   # Categories
#   if 'categories' in request.GET:
#     category = request.GET['category']
#     if category:
#       queryset_list = queryset_list.filter(category__iexact=category)

#   context = {
#     'sellers': queryset_list,
#   }

#   return render(request, 'sellers/search.html', context)
