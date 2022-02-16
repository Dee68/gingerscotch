from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField

# Create your models here.

class Service(models.Model):
    ICON_STATUS = (
        ('calendar','calendar'),
        ('clapperboard','clapperboard'),
        ('drive','drive'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True,unique=True)
    description = RichTextUploadingField()#models.TextField()
    image = CloudinaryField('image')#models.ImageField(blank=True, null=True)
    icon = models.CharField(max_length=20, choices=ICON_STATUS, default='calendar')
    contract = RichTextUploadingField(blank=True, null=True)
    


    def __str__(self):
        return self.title


    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" height="50" width="50">' %self.image.url)
        return "No image found"
