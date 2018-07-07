from django import forms
from .models import Brand, Model, Product, ProductModel


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'brand']


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['product', 'model']
