from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models.aggregates import Avg

FLAG_TYPES = (
    ('Sale', 'Sale'),
    ('New', 'New'),
    ('Feature','Feature'),

)
class Product(models.Model):
    name = models.CharField( _('Name'), max_length=120)
    flag = models.CharField(_('Flag'),max_length=10, choices=FLAG_TYPES)
    image = models.ImageField(_('Image'),upload_to='image_psoduct')
    price = models.FloatField(_('Price'),)
    sku = models.CharField(_('SKU'),max_length=12)
    subtitle = models.CharField(_('Subtitle'),max_length=300)
    dsecreiption = models.TextField(_('Dsecreiption'),max_length=5000)
    quantity = models.IntegerField(_('Quantity'))
    brand = models.ForeignKey('Brand' , verbose_name=_('Brands'), related_name='product_brand', on_delete=models.SET_NULL , null=True)
    tags = TaggableManager(_('TAGS'))
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Product, self).save(*args, **kwargs)


    def avg_rate(self):
        avg = self.product_reviews.aggregate(rate_avg=Avg('rate'))
        if not  avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']

class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('Product-Images'), related_name='product_image', on_delete=models.SET_NULL , null=True)
    image = models.ImageField( _('Product-Images-Upload'), upload_to='product_image')
    def __str__(self):
        return str(self.product)

class Brand(models.Model):
    name = models.CharField( _('Name'), max_length=100)
    image = models.ImageField(_('Brand-Images-Upload'),upload_to='brands')
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Brand, self).save(*args, **kwargs)

class Review(models.Model):
    user = models.ForeignKey( User , verbose_name=_('User-Review'), related_name='user_reviews', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product , verbose_name=_('Product-Review'), related_name='product_reviews', on_delete=models.CASCADE)
    rate = models.IntegerField(_('Rate-Review'))
    review = models.CharField( _('Review'), max_length=500)
    created_at = models.DateTimeField( _('Created_at-Review'), default=timezone.now)
    def __str__(self):
        return f"{self.user}-{self.product}"