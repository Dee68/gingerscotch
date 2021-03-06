from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', True),
        ('False', False),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=20)
    fax = models.CharField(blank=True, max_length=20) 
    email = models.EmailField(blank=True, max_length=50)
    icon = CloudinaryField('image')#models.ImageField(blank=True, upload_to='icons/')
    facebook = models.CharField(blank=True, max_length=20)
    instagram = models.CharField(blank=True, max_length=20)
    twitter = models.CharField(blank=True, max_length=20)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=20)
    smtpport = models.CharField(blank=True, max_length=20)
    aboutus = RichTextUploadingField()#models.TextField()
    contact = RichTextUploadingField()#models.TextField()
    #references = models.TextField()
    status = models.CharField(max_length=5, choices=STATUS, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
        STATUS = (
            ('New','New'),
            ('Closed','Closed'),
            ('Read','Read'),
        )
        name = models.CharField(max_length=50)
        email = models.EmailField(max_length=100)
        subject = models.CharField(max_length=150)
        message = models.TextField(max_length=255)
        ip = models.CharField(blank=True, max_length=50)
        note = models.CharField(blank=True, max_length=50)
        status = models.CharField(max_length=6, choices=STATUS, default='New')
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name+" - message"

class SubscribedUser(models.Model):
    email = models.EmailField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.email