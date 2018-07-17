from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Brand, Model, Product, ProductModel
from .forms import BrandForm, ModelForm, ProductForm, ProductModelForm
from rest_framework import mixins, generics, permissions
from catalog.serializers import BrandSerializer


class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'


class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm


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
