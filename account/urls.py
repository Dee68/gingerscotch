from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    RegistrationView, 
    LoginView, 
    LogoutPage,
    ProfileView,
    ProfileUpdate,
    WishListView,
    add_to_whishlist,
    VerificationView,
    UsernamevalidationView, 
    EmailValidation,
    ManageUserRegister,
    CustomUserRegister)
from django.views.decorators.csrf import csrf_exempt

app_name = 'account'

urlpatterns = [
    path('register/',RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutPage.as_view(), name='logout'),
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    path('profile-update/', ProfileUpdate.as_view(), name='profile-update'),
    path('whishlist/', WishListView.as_view(), name='whishlist'),
    path('add-to-whishlist/<int:id>/', add_to_whishlist, name='add-to-whishlist'),
    path('validate-username', csrf_exempt(UsernamevalidationView.as_view()), name='validate-username'),
    path('activate/<uidb64>/<token>/', VerificationView.as_view(), name='activate'),
    path('validate-email', csrf_exempt(EmailValidation.as_view()), name='validate-email'),
    path('register/manager/', ManageUserRegister.as_view(), name='manager-registration'),
    path('register/customer/', CustomUserRegister.as_view(), name='customer-registration'),
]