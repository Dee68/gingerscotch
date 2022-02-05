"""gingerscotch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('products/', include('product.urls', namespace='product')),
    path('account/', include('account.urls', namespace='account')),
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    # authentication views from django framework
    path('account/password-change/', login_required(auth_views.PasswordChangeView.as_view(template_name='account/password_change.html')), 
    name='password-change'), 
    path('account/password-change/done/', login_required(auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html')), 
    name='password_change_done'),
    # ========================
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), 
    name='password_reset'),
     path('reset_password/done/', 
    auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'), 
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_form.html'), 
    name='password_reset_confirm'),
    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), 
    name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Inuwa Agro Administration'
admin.site.index_title = 'Manage Inuwa Agro-Poultry Hatchery LTD'
admin.site.site_title = 'InuwaAgro admin'
