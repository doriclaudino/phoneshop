from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Brand
from .forms import BrandForm


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

