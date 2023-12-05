from django.db import models
import datetime
import os
from django.shortcuts import reverse
# Create your models here.

ISO_date = "2021-12-18"
default_date= datetime.date.fromisoformat(ISO_date)

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)


class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    new_arrivals = models.BooleanField(default=False, help_text="0=default, 1=new_arrivals")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    Selling_price = models.FloatField(null=False, blank=False)
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
    new_arrivals = models.BooleanField(default=False, help_text="0=default, 1=new_arrivals")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/images/c.jpeg"
    
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    # Username = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    ConfirmPassword = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField( default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Reviews"
    
    def __str__(self):
        return self.product.name
    
    def get_rating(self):
        return self.rating
        