from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse,HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, FormView,CreateView,DetailView
from .models import *
from .forms import ReviewForm
from account.models import CustomUser
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

class ProductListView(ListView):
    context_object_name = 'products'
    paginate_by = 6
    model = Product
    template_name = 'product/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = "products"
        return context


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


@login_required
def add_review(request, id):
    product = get_object_or_404(Product, id=id)
    form = ReviewForm(request.POST)
    context = {'form':form}
    if 'review' in request.POST:
        proid = request.POST.get('proid')
        if form.is_valid():
            data = Review()
            data.name = form.cleaned_data.get('name')
            data.message = form.cleaned_data.get('message')
            data.rating = form.cleaned_data.get('rating')
            data.ip = request.META.get('REMOTE_ADDR')
            data.product = proid
            data.user = request.user
            data.save()
            messages.success(request, 'review added successfully.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render(request, 'product/product_detail.html', context)

# class AddReview(CreateView):
#     model = Review
#     template_name = 'product/product_review.html'
#     form_class = ReviewForm
#     success_url = reverse_lazy('product:products')
    
#     def form_valid(self, form):
#         form.instance.product_id = self.kwargs['id']
#         form.instance.ip = self.request.META.get('REMOTE_ADDR')
#         form.instance.name = self.request.user
#         # form.instance.next = self.request.POST.get('next')
#         return super().form_valid(form)

    



class ReviewDisplay(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        product = self.object
        ppictures = Picture.objects.filter(product=product)
        specifications = product.specification.split(",")
        context['ppictures'] = ppictures
        context['specifications'] = specifications
        context['form'] = ReviewForm()
        return context

class Reviewproduct(SingleObjectMixin, FormView):
    model = Product
    form_class = ReviewForm
    template_name = 'product/product_review.html'  

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(Reviewproduct, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        review = form.save(commit=False)
        review.product = self.object
        review.ip = self.request.META.get('REMOTE_ADDR')
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        product = self.object
        return reverse('product:product-detail', kwargs={'id':product.id,'slug':product.slug})+'#reviews'


class ProductDetail(View):
    def get(self, request, *args, **kwargs):
        view = ReviewDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = Reviewproduct.as_view()
        return view(request, *args, **kwargs)
    # def get(self, request, id, slug):
    #     product = get_object_or_404(Product, id=id, slug=slug)
    #     # review = get_object_or_404(Review, product=product.id)
    #     ppictures = Picture.objects.filter(product=product)
    #     specifications = product.specification.split(",")
    #     context = {'product':product,'ppictures':ppictures,'specifications':specifications}
    #     return render(request, 'product/product_detail.html', context)

