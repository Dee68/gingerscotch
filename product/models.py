from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False,unique=True,max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='categories/')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" height="50" width="50">' %self.image.url)
        return "No image found"


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False,unique=True)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=True)
    specification = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    details = models.TextField()
    image = models.ImageField(blank=True, upload_to='products/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" height="50" width="50">' %self.image.url)
        return "No image found"


class Picture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True, upload_to='pictures/')

    def __str__(self):
        return self.title


    
    