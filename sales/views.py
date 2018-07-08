from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Seller, SellOrderStatus, SellOrder, SellOrderItem
from .forms import SellerForm, SellOrderStatusForm, SellOrderForm, SellOrderItemForm


class SellerListView(ListView):
    model = Seller


class SellerCreateView(CreateView):
    model = Seller
    form_class = SellerForm


class SellerDetailView(DetailView):
    model = Seller


class SellerUpdateView(UpdateView):
    model = Seller
    form_class = SellerForm


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
