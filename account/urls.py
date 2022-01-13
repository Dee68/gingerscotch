from django.urls import path
from .views import (
    register_view,
    RegistrationView, 
    LoginView, 
    UsernamevalidationView, 
    EmailValidation,
    CustomerCreate,
    CustomUserRegister)
from django.views.decorators.csrf import csrf_exempt

app_name = 'account'

urlpatterns = [
    path('register/',RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('validate-username', csrf_exempt(UsernamevalidationView.as_view()), name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidation.as_view()), name='validate-email'),
    # path('register/customer/', CustomerCreate.as_view(), name='customer-registration'),
    path('register/customer/', CustomUserRegister.as_view(), name='customer-registration'),
]