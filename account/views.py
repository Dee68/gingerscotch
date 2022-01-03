from django.shortcuts import render
from django.views import View
# Create your views here.

class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'account/register.html', context)

    def post(self,request, *args, **kwargs):
        pass


class LoginView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'account/login.html', context)

    def post(self, request, *args, **kwargs):
        pass