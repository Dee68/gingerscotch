from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.db import transaction
from django.views.generic import TemplateView, FormView, CreateView
from .models import CustomUser, Profile, Customer, Manager
from product.models import Category,Product, Picture
from .forms import CustomerCreationForm, ManagerCreationForm,LoginForm, ProfileUpdateForm, UserUpdateForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.core.validators import validate_email
from django.http import JsonResponse,HttpResponseRedirect
from .utils import token_generator

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
            user.is_active = False
            user.save()
            user.refresh_from_db()
            customer = Customer.objects.create(user=user)
            customer.address = form.cleaned_data.get('address')
            customer.postal_code = form.cleaned_data.get('postal_code')
            customer.save()  
            email_subject = 'Account activation'
            # path to view
            #-get domain
            #-token
            #-uidb64
            uidb64 =urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('account:activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
            activate_url = 'http://'+domain+link
            email_body = 'Hi '+user.username+',please use the link below to activate your account\n'+activate_url
            send_mail(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [form.cleaned_data.get('email')],
                fail_silently=False
            )
            
            messages.success(request,mark_safe("Account created successfully.<br>Check your mail to activate account."))
            return render(request, 'account/customer_register.html', context)
        else:
            messages.error(request,"Invalid form, please fill in all fields.")
            return render(request, 'account/customer_register.html', context)

class VerificationView(View):
    def get(self,request,uidb64,token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=id)
            if not token_generator.check_token(user,token):
                messages.warning(request,'Account already activated')
                return redirect('home:home')
            if user.is_active:
                return redirect('account:login')
            user.is_active = True
            user.save()
            messages.success(request,'Account successfully activated')
        except Exception as ex:
            pass
        return redirect('account:login')


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
            user.is_active = False
            user.set_password(password1)
            user.save()
            user.refresh_from_db()
            manager = Manager.objects.create(user=user)
            manager.department = form.cleaned_data.get('department')
            manager.phone = form.cleaned_data.get('phone')
            manager.address = form.cleaned_data.get('address')
            manager.save() 
            email_subject = 'Account activation'
            # path to view
            #-get domain
            #-token
            #-uidb64
            uidb64 =urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('account:activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
            activate_url = 'http://'+domain+link
            email_body = 'Hi '+user.username+',please use the link below to activate your account\n'+activate_url
            send_mail(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [form.cleaned_data.get('email')],
                fail_silently=False
            )
            
            messages.success(request,mark_safe("Account created successfully.<br>Check your mail to acivate account."))
            return render(request, 'account/manager_register.html', context)
        else:
            messages.error(request,"Invalid form, please fill in all fields.")
            return render(request, 'account/manager_register.html', context)


    

class UsernamevalidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            data['username_error'] = 'Username should contain only alphanumeric characters.'
            return JsonResponse(data, status=400)
        if CustomUser.objects.filter(username=username).exists():
            data['username_error'] = 'Sorry username already in use, choose another.'
            return JsonResponse(data, status=409)
        data['username_valid'] = True
        return JsonResponse(data, status=200)

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
            if user is not None:
                if user.is_active:
                    login(request,user)
                    if user.is_customer:
                        messages.success(request, 'Welcome, '+user.username)
                        return redirect('home:home')
                    else:
                        category = Category.objects.filter(slug='birds')
                        return render(request, 'account/manager_admin.html', {'category':category})  
                # elif user.is_active== False and CustomUser.objects.filter(username=username).exists():
                #     messages.error(request,'Account not activated,please check your mail to activate.')
                    return render(request, 'account/login.html',context)
            elif user is None and CustomUser.objects.filter(username=username,is_active=True).exists():
                messages.error(request,'Invalid credentials, please try again.')
                return render(request, 'account/login.html',context)
            elif user is None and CustomUser.objects.filter(username=username,is_active=False).exists():
                 messages.info(request,'Account not activated,please check your mail to activate.')
                 return render(request, 'account/login.html',context)
            else:
                messages.error(request,'Please register to login to the system.')
                return render(request, 'account/login.html',context)
           
        messages.error(request, 'Please fill all fields to login')
        return render(request, 'account/login.html',context)

        

class LogoutPage(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home:home')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        userprofile = get_object_or_404(Profile,user=request.user)
        context = {'userprofile':userprofile,'nbar':'profile'}
        return render(request, 'account/profile.html', context)



class ProfileUpdate(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        userprofile = get_object_or_404(Profile, user=request.user)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=userprofile)
        context = {'userprofile':userprofile,'user_form':user_form,'profile_form':profile_form}
        return render(request, 'account/profile_update.html', context)

    def post(self, request, *args, **kwargs):
        userprofile = get_object_or_404(Profile, user=request.user)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=userprofile)
        context = {'userprofile':userprofile,'user_form':user_form,'profile_form':profile_form}
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile has been updated.')
            return redirect('account:profile')
        else:
            return render(request, 'account/profile_update.html',context)


class WishListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(users_wishlist=request.user)
        context = {'products':products}
        return render(request, 'account/whishlist.html', context)





class AddToWhishList(LoginRequiredMixin,TemplateView):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        if product.users_wishlist.filter(id=request.user.id).exists():
            product.users_wishlist.remove(request.user)
            messages.warning(request, product.name +' removed from whishlist.')
        else:
            product.users_wishlist.add(request.user)
            messages.success(request, product.name+' added to whishlist.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

   