from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Supplier
from .forms import SupplierForm


class SupplierListView(ListView):
    model = Supplier


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm


class SupplierDetailView(DetailView):
    model = Supplier


class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm

