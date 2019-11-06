from django.db import models
from datetime import datetime

from sellers.models import Seller
from .choices import category, badge

category_list = [
    ('select a category', 'SELECT A CATEGORY'),
    ('antiques', 'ANTIQUES'),
    ('books', 'BOOKS'),
    ('cameras', 'CAMERAS'),
    ('collectibles', 'COLLECTIBLES'),
    ('dolls', 'DOLLS'),
    ('electronics', 'ELECTRONICS'),
    ('flatware', 'FLATWARE'),
    ('furniture', 'FURNITURE'),
    ('games', 'GAMES'),
    ('glassware', 'GLASSWARE'),
    ('household items', 'HOUSEHOLD ITEMS'),
    ('jewelry', 'JEWELRY'),
    ('knick knacks', 'KNICK KNACKS'),
    ('mens fashion', 'MENS FASHION'),
    ('miscellaneous', 'MISCELLANEOUS'),
    ('movies - dvd', 'MOVIES - DVD'),
    ('movies - vhs', 'MOVIES - VHS'),
    ('music - all', 'MUSIC - ALL'),
    ('music - cd', 'MUSIC - CD'),
    ('music - vinyl', 'MUSIC - VINYL'),
    ('novely items', 'NOVELTY ITEMS'),
    ('posters', 'POSTERS'),
    ('shoes', 'SHOES'),
    ('tools - all', 'TOOLS - ALL'),
    ('tools - hand tools', 'TOOLS - HAND TOOLS'),
    ('tools - power tools', 'TOOLS - POWER TOOLS'),
    ('tools - yard tools', 'TOOLS - YARD TOOLS'),
    ('womens fashion', 'WOMENS FASHION'),
    ('writing utensils', 'WRITING UTENSILS'),
]

badge = [
    ('none', 'NONE'),
    ('special', 'SPECIAL'),
]

class Item(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=70)
    item_badge = models.CharField(max_length=20, choices=badge)
    category_list = models.CharField(max_length=50, choices=category_list)
    photo_main = models.ImageField(upload_to='media/%Y%/m%/%d', blank=False)
    photo_front = models.ImageField(upload_to='media/%Y%/m%/%d', blank=True)
    photo_back = models.ImageField(upload_to='media/%Y%/m%/%d', blank=True)
    is_published = models.BooleanField(default=True)
    date_listed = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title