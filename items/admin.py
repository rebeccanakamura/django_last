from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'date_listed', 'seller')
    list_display_links = ('id', 'title')
    list_filter = ('seller', 'date_listed')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'seller', 'category')
    list_per_page = 20

admin.site.register(Item, ItemAdmin)
