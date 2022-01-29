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


class ShowSubCategory(View):
    def get(self, request, cat_slug=None):
        if cat_slug:
            cat = get_object_or_404(Category,slug=cat_slug)
            products = Product.objects.filter(category=cat)
        
        return render(request, 'product/sub_category.html', {'products':products,'cat':cat})

class AllCategories(View):
    def get(self, request):
        categories = Category.objects.filter(parent__isnull=False)
        context = {'categories':categories}
        return render(request, 'product/allcategories.html', context)