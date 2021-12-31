from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
# Create your views here.

class ProductListView(ListView):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'product/home.html',context)
