from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from cloudinary.models import CloudinaryField
from django.conf import settings
# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False,unique=True,max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = CloudinaryField('image')#models.ImageField(blank=True, upload_to='categories/')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" height="50" width="50">' %self.image.url)
        return "No image found"


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False,unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=True)
    specification = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    details = models.TextField()
    image = CloudinaryField('image')#models.ImageField(blank=True, upload_to='products/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,related_name='users_wishlist')

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" height="50" width="50">' %self.image.url)
        return "No image found"


class Picture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image')#models.ImageField(blank=True, upload_to='pictures/')

    def __str__(self):
        return self.title


    
    