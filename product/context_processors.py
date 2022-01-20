from .models import Category,Product

def access_parent_category(request):
    """ returns a dictionary """
    pcategories = Category.objects.filter(parent=None)
    products = Product.objects.all()
    return {'pcategories':pcategories,'products':products}