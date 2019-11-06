from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='sellers'),
    path('<int:seller_id>', views.seller, name='seller'),
    path('search', views.search, name='search'),
]
