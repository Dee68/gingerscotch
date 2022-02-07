from re import M
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Profile, Customer, Manager
from django.db import transaction


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Username','name':'username','id':'usernameField','value':""}))
    first_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class':'text','placeholder':'Firstname','name':'firstname','id':'firstnameField','value':""}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Lastname','name':'lastname','id':'lastnameField','value':""}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'text','placeholder':'Email','name':'email','id':'emailField','value':""}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text','placeholder':'Password','name':'password1','id':'password1Field'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text w3lpass','name':'password2','id':'password2Field','placeholder':'Confirm Password'}))
    # user_type = forms.CharField(max_length=100,widget=forms.RadioSelect(attrs={'class':'checkbox','id':'user_type','name':'user_type'}))
    is_customer = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'text','id':'customer','name':'customer'}))
    is_manager = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'text','id':'manager','name':'manager'}))
    # departments = (('sales','Sales'),('production','Production'))
    # department = forms.ChoiceField(choices=departments, widget=forms.RadioSelect(attrs={'class':'checkbox','id':'department','name':'department'}))
    


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name','email','password1','password2','is_customer','is_manager')


class CustomerCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Username','name':'username','id':'usernameField','value':""}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'text','placeholder':'Firstname','name':'firstname','id':'firstnameField','value':""}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'text','placeholder':'Lastname','name':'lastname','id':'lastnameField','value':""}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'text','placeholder':'Email','name':'email','id':'emailField','value':""}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text','placeholder':'Password','name':'password1','id':'password1Field'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text w3lpass','name':'password2','id':'password2Field','placeholder':'Confirm Password'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Address','name':'address','id':'address','value':""}))
    postal_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Postal_Code','name':'postal_code','id':'postal_code','value':""}))


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name','email','password1','password2','address','postal_code')

    
  


class ManagerCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Username','name':'username','id':'usernameField','value':""}))
    first_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class':'text','placeholder':'Firstname','name':'firstname','id':'firstnameField','value':""}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Lastname','name':'lastname','id':'lastnameField','value':""}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'text','placeholder':'Email','name':'email','id':'emailField','value':""}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text','placeholder':'Password','name':'password1','id':'password1Field'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text w3lpass','name':'password2','id':'password2Field','placeholder':'Confirm Password'}))
    departments = (('sale','Sale'),('production','Production'),)
    department = forms.ChoiceField(choices=departments, widget=forms.RadioSelect(attrs={'class':'checkbox','id':'department','name':'department'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Telephone','name':'phone','id':'phone','value':""}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Address','name':'address','id':'address','value':""}))
    


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name','email','password1','password2','department','phone','address')

    
class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','placeholder':'Username','name':'username','id':'usernameField','value':""}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'text','placeholder':'Password','name':'password','id':'passwordField'}))
    class Meta:
        model = CustomUser
        fields = ('username','password')




genders = (('male','male'),('female','female'),)

class ProfileUpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=genders, widget=forms.RadioSelect(attrs={'placeholder':'gender'}))
    bio = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter bio ...'}))
    phone = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telephone'}))
    country = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'city'}))
    occupation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'occupation'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address'}))
    company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'company'}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Upload your avatar'}))
    class Meta:
        model = Profile
        fields = ['gender','bio','phone','country','city','occupation','address','company','avatar']


class UserUpdateForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','name':'username','id':'usernameField','value':""}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','id':'email','placeholder':'Enter Email','name':'email','value':''}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first_name','name':'first_name','id':'firstnameField','value':""}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last_name','name':'last_name','id':'lastnameField','value':""}))
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name']

    
        