from django.contrib import admin
from .models import Category, Picture, Product, Cart, Order, ShippingAddress, Notification, Review
from mptt.admin import DraggableMPTTAdmin
# Register your models here.
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count','image_tag')
    list_display_links = ('indented_title',)
    readonly_fields = ['image_tag']
    prepopulated_fields = {'slug':('name',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','image_tag','in_stock', 'price','category']
    list_filter = ['in_stock','created','updated']
    list_editable = ['price','in_stock']
    readonly_fields = ['image_tag']
    prepopulated_fields = {'slug':('name',)}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name','message','rating']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Picture)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(ShippingAddress)
admin.site.register(Notification)
admin.site.register(Review,ReviewAdmin)