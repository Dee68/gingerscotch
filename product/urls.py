from django.urls import path
from .views import ProductListView,ShowCategory,ShowSubCategory,AllCategories,ProductDetail

app_name = 'product'

urlpatterns = [
    # shows products of all categories
    path('',ProductListView.as_view(), name='products'),
    # shows all Categories
    path('allcategories/', AllCategories.as_view(), name='allcategories'),
    # shows a parent category
    path('category/<str:category_slug>/',ShowCategory.as_view(), name='show-category'),
    # shows products of subcategory
    path('<str:cat_slug>/', ShowSubCategory.as_view(), name='show-subcategory'),
    # shows product Details
    path('<int:id>/<str:slug>/',ProductDetail.as_view(), name='product-detail'),
    
]