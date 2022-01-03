from django.db import models

# Create your models here.

# class Setting(models.Model):
#     pass


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