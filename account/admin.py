from django.contrib import admin
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    fieldsets = (*UserAdmin.fieldsets, (
        'User Role', { 'fields':(
            'is_customer',
            'is_manager',
            'is_admin'
        )

        }
    ))

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)