from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import *
# Create your views here.

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        context = {'nbar': 'products'} 
        return render(request, 'product/home.html',context)


class ShowCategory(View):
    def get(self, request, category_slug):
        pcat = get_object_or_404(Category,slug=category_slug)
        categories = Category.objects.filter(parent=pcat)
        return render(request,'product/category.html',{'categories':categories,'pcat':pcat})
