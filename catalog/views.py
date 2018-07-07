from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Brand, Model
from .forms import BrandForm, ModelForm


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
