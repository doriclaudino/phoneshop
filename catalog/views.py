from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Brand, Model, Product, ProductModel
from .forms import BrandForm, ModelForm, ProductForm, ProductModelForm


class BrandListView(ListView):
    model = Brand


class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm


class BrandDetailView(DetailView):
    model = Brand


class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm


class ModelListView(ListView):
    model = Model


class ModelCreateView(CreateView):
    model = Model
    form_class = ModelForm


class ModelDetailView(DetailView):
    model = Model


class ModelUpdateView(UpdateView):
    model = Model
    form_class = ModelForm


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


class ProductModelListView(ListView):
    model = ProductModel


class ProductModelCreateView(CreateView):
    model = ProductModel
    form_class = ProductModelForm


class ProductModelDetailView(DetailView):
    model = ProductModel


class ProductModelUpdateView(UpdateView):
    model = ProductModel
    form_class = ProductModelForm
