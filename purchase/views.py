from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Supplier, PurchaseOrderStatus, PurchaseOrder, PurchaseOrderItem
from .forms import SupplierForm, PurchaseOrderStatusForm, PurchaseOrderForm, PurchaseOrderItemForm


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


class PurchaseOrderListView(ListView):
    model = PurchaseOrder


class PurchaseOrderCreateView(CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm


class PurchaseOrderDetailView(DetailView):
    model = PurchaseOrder


class PurchaseOrderUpdateView(UpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm


class PurchaseOrderItemListView(ListView):
    model = PurchaseOrderItem


class PurchaseOrderItemCreateView(CreateView):
    model = PurchaseOrderItem
    form_class = PurchaseOrderItemForm


class PurchaseOrderItemDetailView(DetailView):
    model = PurchaseOrderItem


class PurchaseOrderItemUpdateView(UpdateView):
    model = PurchaseOrderItem
    form_class = PurchaseOrderItemForm
