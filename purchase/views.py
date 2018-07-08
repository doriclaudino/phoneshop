from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Supplier, PurchaseOrderStatus
from .forms import SupplierForm, PurchaseOrderStatusForm


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


class PurchaseOrderStatusListView(ListView):
    model = PurchaseOrderStatus


class PurchaseOrderStatusCreateView(CreateView):
    model = PurchaseOrderStatus
    form_class = PurchaseOrderStatusForm


class PurchaseOrderStatusDetailView(DetailView):
    model = PurchaseOrderStatus


class PurchaseOrderStatusUpdateView(UpdateView):
    model = PurchaseOrderStatus
    form_class = PurchaseOrderStatusForm
