from django import forms
from .models import Product, Category, Brand, Supplier, Feature

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'})}

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand Name'})}

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'location', 'country_code', 'is_verified']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplier Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Lahore'}),
            'country_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'pk'}),
            'is_verified': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Feature Name'})}

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'supplier', 'features', 'condition', 'prev_price', 'new_price', 'discount_percentage', 'tax_percentage', 'image', 'description', 'stock', 'sold_count', 'rating', 'is_featured']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Title'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'supplier': forms.Select(attrs={'class': 'form-select'}),
            'features': forms.SelectMultiple(attrs={'class': 'form-select', 'rows': 4}), 
            'condition': forms.Select(attrs={'class': 'form-select'}),
            'prev_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'new_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'discount_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'tax_percentage': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Product description...'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'sold_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'max': '5.0'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'transform: scale(1.5); margin-left: 5px;'}),
        }