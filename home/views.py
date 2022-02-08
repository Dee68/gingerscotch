from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import messages
from product.models import *
from .models import *
from .forms import ContactMessageForm,SubscribersForm
from django.views.generic import TemplateView,ListView, FormView
from django.views import View
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.

class ProductList(ListView):
    model = Product
    template_name='home/index.html'
    context_object_name = "products"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SubscribersForm
        return context

class SubscriberAdd(FormView):
    template_name = 'home/index.html'
    form_class = SubscribersForm
    model = SubscribedUser

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            data = SubscribedUser()
            data.email = form.cleaned_data.get('email')
            if SubscribedUser.objects.filter(email=data.email).exists():
                messages.warning(request,'This email already exists in our database.')
                return HttpResponseRedirect('/')
            else:
                data.save()
                messages.success(request,'Subscription successful')
                return HttpResponseRedirect('/')
        context = {'form':form}
        return render(request, 'home/index.html', context)

class ShopList(View):
    def get(self, request, *args, **kwargs):
        view = ProductList.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = SubscriberAdd.as_view()
        return view(request, *args, **kwargs)

class AboutUs(TemplateView):
    template_name = 'home/about.html'


class ContactUs(View):
    def get(self, request, *args, **kwargs):
        form = ContactMessageForm()
        context = {'form':form}
        return render(request, 'home/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data.get('name')
            data.email = form.cleaned_data.get('email')
            data.subject = form.cleaned_data.get('subject')
            data.message = form.cleaned_data.get('message')
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Message successfully sent, we will get back to you soon.")
            return HttpResponseRedirect('/contact')
        messages.error(request,'Please fill all fields carefully.')
        context = {'form':form}
        return render(request, 'home/contact.html', context)