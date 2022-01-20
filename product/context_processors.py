from .models import Category

def access_parent_category(request):
    """ returns a dictionary """
    pcategories = Category.objects.filter(parent=None)
    return {'pcategories':pcategories}