from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        context = {'nbar': 'products'} 
        return render(request, 'product/home.html',context)
