from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Customer, Manager
from django.db import transaction


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Username','name':'username','id':'usernameField','value':""}))
    first_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class':'text','placeholder':'Firstname','name':'firstname','id':'firstnameField','value':""}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Lastname','name':'lastname','id':'lastnameField','value':""}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'text','placeholder':'Email','name':'email','id':'emailField','value':""}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text','placeholder':'Password','name':'password1','id':'password1Field'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text w3lpass','name':'password2','id':'password2Field','placeholder':'Confirm Password'}))
    user_type = forms.CharField(max_length=100,widget=forms.RadioSelect(attrs={'class':'checkbox','id':'user_type','name':'user_type'}))
    # is_customer = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'text','id':'customer','name':'customer'}))
    # is_manager = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'text','id':'manager','name':'manager'}))
    # departments = (('sales','Sales'),('production','Production'))
    # department = forms.ChoiceField(choices=departments, widget=forms.RadioSelect(attrs={'class':'checkbox','id':'department','name':'department'}))
    


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name','email','password1','password2','user_type')


class CustomerCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Username','name':'username','id':'usernameField','value':""}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'text','placeholder':'Firstname','name':'firstname','id':'firstnameField','value':""}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'text','placeholder':'Lastname','name':'lastname','id':'lastnameField','value':""}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'text','placeholder':'Email','name':'email','id':'emailField','value':""}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text','placeholder':'Password','name':'password1','id':'password1Field'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text w3lpass','name':'password2','id':'password2Field','placeholder':'Confirm Password'}))
    # is_customer = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'text','id':'customer','name':'customer'}))
    # is_manager = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'text','id':'manager','name':'manager'}))
    # departments = (('sales','Sales'),('production','Production'))
    # department = forms.ChoiceField(choices=departments, widget=forms.RadioSelect(attrs={'class':'checkbox','id':'department','name':'department'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Address','name':'address','id':'address','value':""}))
    postal_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Postal_Code','name':'postal_code','id':'postal_code','value':""}))


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name','email','password1','password2','address','postal_code')

    
    # def data_save(self):
    #     with transaction.atomic():
    #         user = super().save(commit=False)
    #         user.user_type = 'customer'
    #         user.save()
    #         customer = Customer.objects.create(user=user)
    #         customer.username.add(*self.cleaned_data.get('username'))
    #         customer.first_name.add(*self.cleaned_data.get('first_name'))
    #         customer.last_name.add(*self.cleaned_data.get('last_name'))
    #         customer.email.add(*self.cleaned_data.get('email'))
    #         customer.address.add(*self.cleaned_data.get('address'))
    #         customer.postal_code.add(*self.cleaned_data.get('postal_code'))
    #         customer.save()
        
    #     return user


class ManagerCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Username','name':'username','id':'usernameField','value':""}))
    first_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class':'text','placeholder':'Firstname','name':'firstname','id':'firstnameField','value':""}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Lastname','name':'lastname','id':'lastnameField','value':""}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'text','placeholder':'Email','name':'email','id':'emailField','value':""}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text','placeholder':'Password','name':'password1','id':'password1Field'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text w3lpass','name':'password2','id':'password2Field','placeholder':'Confirm Password'}))
    departments = (('sale','Sale'),('production','Production'),)
    department = forms.ChoiceField(choices=departments, widget=forms.RadioSelect(attrs={'class':'checkbox','id':'gender','name':'gender'}))
    postal_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Telephone','name':'phone','id':'phone','value':""}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Address','name':'address','id':'address','value':""}))
    


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name','email','password1','password2','department','address','postal_code')
    
        