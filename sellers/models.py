from django.db import models
from datetime import datetime

class Seller(models.Model):
    name = models.CharField(max_length=100)
    sellerAddress1 = models.CharField(max_length=100)
    sellerAddress2 = models.CharField(max_length=100, blank=True)
    sellerCity = models.CharField(max_length=100)
    sellerState = models.CharField(max_length=20)
    sellerZipcode = models.CharField(max_length=10)
    sellerEmail = models.CharField(max_length=100)
    sellerPhone = models.CharField(max_length=20)
    sellerPhoto = models.ImageField(upload_to='media/%Y%/m%/%d', default=False)
    description = models.TextField()
    isSellerOfMonth = models.BooleanField(default=False)
    dateJoined = models.DateTimeField(default=datetime.now, blank=False)
    itemsListed = models.TextField(blank=True)
    itemAdded = models.DateTimeField(default=datetime.now, blank=False)
    def __str__(self):
        return self.name