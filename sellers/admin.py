from django.contrib import admin

from .models import Seller

class SellerAdmin(admin.ModelAdmin):
    listDisplay = ('id', 'name', 'dateJoined')
    listDisplay_links = ('id', 'name')
    searchFields = ('name',)
    listPerPage = 10


admin.site.register(Seller, SellerAdmin)