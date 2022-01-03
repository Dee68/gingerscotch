from django.shortcuts import render
from django.views.generic.base import View
from product.models import *
from .models import *
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.list import ListView
# Create your views here.

class ShopList(ListView):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home/index.html',context)

class AboutUs(TemplateView):
    template_name = 'home/about.html'


class ContactUs(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home/contact.html', context)

    def post(self, request, *args, **kwargs):
        pass