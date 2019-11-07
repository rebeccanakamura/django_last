from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isPublished', 'dateListed', 'seller')
    list_display_links = ('id', 'title')
    list_filter = ('seller', 'dateListed')
    list_editable = ('isPublished',)
    search_fields = ('title', 'description', 'seller', 'category')
    list_per_page = 20

admin.site.register(Item, ItemAdmin)
