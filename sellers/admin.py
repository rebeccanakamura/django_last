from django.contrib import admin

from .models import Seller

class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_joined')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10


admin.site.register(Seller, SellerAdmin)