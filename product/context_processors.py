from .models import Category,Product, Picture


def access_parent_category(request):
    """ returns a dictionary """
    pcategories = Category.objects.filter(parent=None)
    products = Product.objects.all()
    pictures = Picture.objects.filter(title__contains='slider')
    return {'pcategories':pcategories,'products':products,'pictures':pictures}