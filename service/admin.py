from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title','icon','image_tag']
    readonly_fields = ['image_tag']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Service,ServiceAdmin)