from django.urls import path
from .views import ProductListView,ShowCategory,ShowSubCategory

app_name = 'product'

urlpatterns = [
    path('',ProductListView.as_view(), name='products'),
    path('category/<str:category_slug>/',ShowCategory.as_view(), name='show-category'),
    path('<str:cat_slug>/', ShowSubCategory.as_view(), name='show-subcategory'),
]