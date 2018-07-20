from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import PaymentMethod, PaymentStatus, SalePayment, PurchasePayment, TrackingPayment
from .forms import PaymentMethodForm, PaymentStatusForm,  SalePaymentForm, PurchasePaymentForm, TrackingPaymentForm


class PaymentMethodListView(ListView):
    model = PaymentMethod


class PaymentMethodCreateView(CreateView):
    model = PaymentMethod
    form_class = PaymentMethodForm


class PaymentMethodDetailView(DetailView):
    model = PaymentMethod


class PaymentMethodUpdateView(UpdateView):
    model = PaymentMethod
    form_class = PaymentMethodForm


class PaymentStatusListView(ListView):
    model = PaymentStatus


class PaymentStatusCreateView(CreateView):
    model = PaymentStatus
    form_class = PaymentStatusForm


class PaymentStatusDetailView(DetailView):
    model = PaymentStatus


class PaymentStatusUpdateView(UpdateView):
    model = PaymentStatus
    form_class = PaymentStatusForm


class SalePaymentListView(ListView):
    model = SalePayment


class SalePaymentCreateView(CreateView):
    model = SalePayment
    form_class = SalePaymentForm


class SalePaymentDetailView(DetailView):
    model = SalePayment


class SalePaymentUpdateView(UpdateView):
    model = SalePayment
    form_class = SalePaymentForm


class PurchasePaymentListView(ListView):
    model = PurchasePayment


class PurchasePaymentCreateView(CreateView):
    model = PurchasePayment
    form_class = PurchasePaymentForm


class PurchasePaymentDetailView(DetailView):
    model = PurchasePayment


class PurchasePaymentUpdateView(UpdateView):
    model = PurchasePayment
    form_class = PurchasePaymentForm


class TrackingPaymentListView(ListView):
    model = TrackingPayment


class TrackingPaymentCreateView(CreateView):
    model = TrackingPayment
    form_class = TrackingPaymentForm


class TrackingPaymentDetailView(DetailView):
    model = TrackingPayment


class TrackingPaymentUpdateView(UpdateView):
    model = TrackingPayment
    form_class = TrackingPaymentForm
