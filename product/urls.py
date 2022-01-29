from django.urls import path
from .views import ProductListView,ShowCategory,ShowSubCategory,AllCategories

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
    
]