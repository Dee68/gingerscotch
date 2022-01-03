from django.urls import path
from .views import ShopList,AboutUs,ContactUs

app_name = 'home'

urlpatterns = [
    path('', ShopList.as_view(), name='home'),
    path('about/', AboutUs.as_view(), name='about'),
    path('contact/', ContactUs.as_view(), name='contact'),
]