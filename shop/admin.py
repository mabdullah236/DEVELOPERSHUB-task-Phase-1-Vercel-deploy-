from django.contrib import admin
from .models import Product, Category, Brand, Supplier, Feature, ProductImage, ProductSpecification

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'new_price', 'stock', 'sold_count', 'is_featured')
    search_fields = ('name', 'category__name', 'brand__name')
    list_filter = ('category', 'is_featured', 'condition', 'brand')
    list_editable = ('new_price', 'stock', 'is_featured')
    list_per_page = 50
    
    inlines = [ProductSpecificationInline, ProductImageInline]

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Supplier)
admin.site.register(Feature)