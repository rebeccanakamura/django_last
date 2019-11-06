from django.db import models
from datetime import datetime

class Seller(models.Model):
    name = models.CharField(max_length=100)
    seller_address_1 = models.CharField(max_length=100)
    seller_address_2 = models.CharField(max_length=100, blank=True)
    seller_city = models.CharField(max_length=100)
    seller_state = models.CharField(max_length=20)
    seller_zipcode = models.CharField(max_length=10)
    seller_email = models.CharField(max_length=100)
    seller_phone = models.CharField(max_length=20)
    seller_photo = models.ImageField(upload_to='media/%Y%/m%/%d', default=False)
    description = models.TextField()
    is_seller_of_month = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.now, blank=False)
    items_listed = models.TextField(blank=True)
    item_added = models.DateTimeField(default=datetime.now, blank=False)
    def __str__(self):
        return self.name