from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Customer, SellOrderStatus, SellOrder, SellOrderItem
from .forms import CustomerForm, SellOrderStatusForm, SellOrderForm, SellOrderItemForm


class CustomerListView(ListView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm


class CustomerDetailView(DetailView):
    model = Customer


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm


class SellOrderStatusListView(ListView):
    model = SellOrderStatus


class SellOrderStatusCreateView(CreateView):
    model = SellOrderStatus
    form_class = SellOrderStatusForm


class SellOrderStatusDetailView(DetailView):
    model = SellOrderStatus


class SellOrderStatusUpdateView(UpdateView):
    model = SellOrderStatus
    form_class = SellOrderStatusForm


class SellOrderListView(ListView):
    model = SellOrder


class SellOrderCreateView(CreateView):
    model = SellOrder
    form_class = SellOrderForm


class SellOrderDetailView(DetailView):
    model = SellOrder


class SellOrderUpdateView(UpdateView):
    model = SellOrder
    form_class = SellOrderForm


class SellOrderItemListView(ListView):
    model = SellOrderItem


class SellOrderItemCreateView(CreateView):
    model = SellOrderItem
    form_class = SellOrderItemForm


class SellOrderItemDetailView(DetailView):
    model = SellOrderItem


class SellOrderItemUpdateView(UpdateView):
    model = SellOrderItem
    form_class = SellOrderItemForm
