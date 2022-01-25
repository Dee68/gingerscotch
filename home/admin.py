from django.contrib import admin
from .models import ContactMessage, SubscribedUser, Setting
# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(SubscribedUser)
admin.site.register(Setting)
