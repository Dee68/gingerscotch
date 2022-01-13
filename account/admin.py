from django.contrib import admin
from .models import CustomUser,Profile,Customer, Manager
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User Type',
            {'fields': ('user_type',)}
        )
    )


    
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Profile)
