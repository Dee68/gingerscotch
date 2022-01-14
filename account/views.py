from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.db import transaction
from django.views.generic import CreateView,TemplateView
from .models import CustomUser, Profile, Customer, Manager
from .forms import CustomerCreationForm, ManagerCreationForm,LoginForm

from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.core.validators import validate_email
from django.http import JsonResponse,HttpResponseRedirect

import json
# Create your views here.

class RegistrationView(TemplateView):
    template_name = 'account/user_type.html'
    
        



class CustomUserRegister(View):
    def get(self, request, *args, **kwargs):
        form = CustomerCreationForm()
        context = {'form':form}
        return render(request, 'account/customer_register.html', context)

    @transaction.atomic
    def post(self,request):
        form = CustomerCreationForm(request.POST)
        fieldVals = request.POST
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        user_email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        context = {"fieldVals":fieldVals, 'form':form}
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "username already in use, choose another one.")
            return render(request, 'account/customer_register.html', context)
        if CustomUser.objects.filter(email=user_email).exists():
            messages.error(request, "sorry email already in use, please choose another one.")
            return render(request, 'account/customer_register.html', context)
        if len(password1) < 8:
            messages.error(request,"password must be 8 characters or more")
            return render(request, 'account/customer_register.html', context)
        if not (password1 == password2):
            messages.error(request, 'passwords did not match')
            return render(request, 'account/customer_register.html', context)
        if (firstname == '' or lastname == ''):
            messages.error(request, mark_safe("Please fill in all fields,<br> they are all required"))
            return render(request, 'account/customer_register.html', context)
            
        if form.is_valid():
            user = form.save()
            user.is_customer = True
            user.set_password(password1)
            user.save()
            user.refresh_from_db()
            customer = Customer.objects.create(user=user)
            customer.address = form.cleaned_data.get('address')
            customer.postal_code = form.cleaned_data.get('postal_code')
            customer.save()   
            messages.success(request,mark_safe("Account created successfully.<br>You can now log in."))
            return render(request, 'account/customer_register.html', context)
        else:
            messages.error(request,"Invalid form, please fill in all fields.")
            return render(request, 'account/customer_register.html', context)

        # return render(request, 'account/customer_register.html', context)


class ManageUserRegister(View):
    def get(self, request, *args, **kwargs):
        form = ManagerCreationForm()
        context = {'form':form}
        return render(request, 'account/manager_register.html', context)

    @transaction.atomic
    def post(self,request):
        form = ManagerCreationForm(request.POST)
        fieldVals = request.POST
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        user_email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        department = request.POST.get('department')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        context = {"fieldVals":fieldVals, 'form':form}
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "username already in use, choose another one.")
            return render(request, 'account/manager_register.html', context)
        if CustomUser.objects.filter(email=user_email).exists():
            messages.error(request, "sorry email already in use, please choose another one.")
            return render(request, 'account/manager_register.html', context)
        if len(password1) < 8:
            messages.error(request,"password must be 8 characters or more")
            return render(request, 'account/manager_register.html', context)
        if not (password1 == password2):
            messages.error(request, 'passwords did not match')
            return render(request, 'account/manager_register.html', context)
        if (firstname == '' or lastname == ''):
            messages.error(request, mark_safe("Please fill in all fields,<br> they are all required"))
            return render(request, 'account/manager_register.html', context)
               
        if form.is_valid():
            user = form.save()
            user.is_manager = True
            user.set_password(password1)
            user.save()
            user.refresh_from_db()
            manager = Manager.objects.create(user=user)
            manager.department = form.cleaned_data.get('department')
            manager.phone = form.cleaned_data.get('phone')
            manager.address = form.cleaned_data.get('address')
            manager.save() 
            messages.success(request,mark_safe("Account created successfully.<br>You can now log in."))
            return render(request, 'account/manager_register.html', context)
        else:
            messages.error(request,"Invalid form, please fill in all fields.")
            return render(request, 'account/manager_register.html', context)

        







    



class UsernamevalidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'Username should contain only alphanumeric characters.'}, status=400)
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'Sorry username already in use, choose another.'}, status=409)
        
        return JsonResponse({'username_valid':True}, status=200)

class EmailValidation(View):
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        if CustomUser.objects.filter(email=email):
            return JsonResponse({'email_error':'Sorry,email already taken, choose another one'},status=409)
        try:
            validate_email(email)
            return JsonResponse({'email_valid':True}, status=200)
        except ValidationError:
            return JsonResponse({'email_error':'Email is invalid'},status=400)
        # if not validate_email(email):
        #     return JsonResponse({'email_error':'Email is invalid'},status=400)
        # if User.objects.filter(email=email):
        #     return JsonResponse({'email_error':'Sorry,email already taken, choose another one'},status=409)
        #return JsonResponse({'email_valid':True})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {'form':form}
        return render(request, 'account/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        context = {'form':form}
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    # messages.success(request, 'Welcome, '+user.username)
                    if user.is_customer:
                        return redirect('home:home')
                    return render(request, 'account/manager_admin.html', context)
                messages.info(request, 'Account not activated, please check your email')
                return render(request, 'account/login.html',context)
            messages.error(request,'Invalid credentials, try again')
            return render(request, 'account/login.html',context)
        messages.error(request, 'Please fill all fields to login')
        return render(request, 'account/login.html',context)

class LogoutPage(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home:home')

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        userprofile = get_object_or_404(Profile,user=request.user)
        context = {'userprofile':userprofile,'nbar':'profile'}
        return render(request, 'account/profile.html', context)