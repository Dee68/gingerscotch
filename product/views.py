from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.views import View
from .models import *
from account.models import CustomUser
from django.contrib import messages
# Create your views here.

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        context = {'nbar': 'products'} 
        return render(request, 'product/home.html',context)


# @login_required(login_url='account/login')
def add_to_cart(request):
    context = {}
    if request.user.is_authenticated:
        items = Cart.objects.filter(customer__id=request.user.id,status=False)
        context['items'] = items
        if request.method == "POST":
            pid = request.POST['pid']
            qty = request.POST['qty']
            do_exist = Cart.objects.filter(product__id=pid, customer__id=request.user.id, status=False)
            if len(do_exist) > 0:
                messages.warning(request,'Item already exists in your cart.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            else:
                product = get_object_or_404(Product, id=pid)
                usr = get_object_or_404(CustomUser,id=request.user.id)
                c = Cart(customer=usr, product=product,quantity=qty)
                c.save()
                messages.success(request, '{}  Added to your cart'.format(product.name))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    else:
        # anonymouse user
        pass
    return render(request, 'product/cart_detail.html', context)

    #using ajax to get cart details
def get_cart_data(request):
    items = Cart.objects.filter(customer__id=request.user.id, status=False)
    # set initial values to 0
    total,quantity,num = 0,0,0
    #loop through items in cart
    for item in items:
        total += float(item.product.price) * item.quantity# cart total
        quantity += int(item.quantity)
        num += 1# number of items in cart
    res = {"total":total,"quantity":quantity,'"num':num}
    return JsonResponse(res)

def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(Cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity)

    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cart_obj = get_object_or_404(Cart,id=id)
        cart_obj.delete()
        return HttpResponse(1)
            


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


class ProductDetail(View):
    def get(self, request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug)
        ppictures = Picture.objects.filter(product=product)
        context = {'product':product,'ppictures':ppictures}
        return render(request, 'product/product_detail.html', context)

