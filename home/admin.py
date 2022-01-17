from django.contrib import admin
from .models import ContactMessage, SubscribedUser
# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(SubscribedUser)
