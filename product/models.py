from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from cloudinary.models import CloudinaryField
from django.conf import settings
from account.models import Customer
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

    def get_absolute_url(self):
        return reverse('product:product-detail',args=[self.id,self.slug])

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

class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total

    def __str__(self):
        return "Cart Id:{} attached to customer:{}".format(str(self.id),str(self.customer))

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    product_ids = models.CharField(max_length=100)
    cart_id = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    invoice_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) :
        return  "Order of ID:{} on this date: {} by {}".format(str(self.id),str(self.date_ordered.strftime('%d /%m/%Y')),str(self.customer))


class ShippingAddress(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = RichTextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for:{self.recipient}"


    
    