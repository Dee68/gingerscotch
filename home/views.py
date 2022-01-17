from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import messages
from product.models import *
from .models import *
from .forms import ContactMessageForm,SubscribersForm
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
# from django.views.generic.list import ListView
# Create your views here.

class ShopList(View):
    def get(self, request, *args, **kwargs):
        form = SubscribersForm()
        context = {'form':form }
        return render(request, 'home/index.html',context)

    def post(self, request, *args, **kwargs):
        form = SubscribersForm(request.POST)
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