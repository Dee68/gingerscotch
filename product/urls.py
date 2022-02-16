from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    ProductListView,
    ShowCategory,
    ShowSubCategory,
    AllCategories,
    ProductDetail,
    # AddReview,
    # Review,
    add_review,
    # ShowReview,
    add_to_cart,
    get_cart_data,
    change_quan)

app_name = 'product'

urlpatterns = [
    # shows products of all categories
    path('',ProductListView.as_view(), name='products'),
    # shows cart
    path('cart/', login_required(add_to_cart), name='cart_details'),
    path('get_cart_data/', get_cart_data, name='get_cart_data'),
    path("change_quan", change_quan, name="change_quan"),

     # add reviews
    path('show-reviews/<int:id>/', add_review, name='show-reviews'),
    
   
    # shows all Categories
    path('allcategories/', AllCategories.as_view(), name='allcategories'),
    # shows a parent category
    path('category/<str:category_slug>/',ShowCategory.as_view(), name='show-category'),
   
    # shows products of subcategory
    path('<str:cat_slug>/', ShowSubCategory.as_view(), name='show-subcategory'),
    # shows product Details
    path('<int:id>/<str:slug>/',ProductDetail.as_view(), name='product-detail'),
    # path('add-review/<int:id>/', AddReview.as_view(), name='add-review'),
    
    
    
]