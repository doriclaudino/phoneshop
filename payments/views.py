from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import PaymentType, PaymentStatus, Payment, OrderPayments
from .forms import PaymentTypeForm, PaymentStatusForm, PaymentForm, OrderPaymentsForm


class PaymentTypeListView(ListView):
    model = PaymentType


class PaymentTypeCreateView(CreateView):
    model = PaymentType
    form_class = PaymentTypeForm


class PaymentTypeDetailView(DetailView):
    model = PaymentType


class PaymentTypeUpdateView(UpdateView):
    model = PaymentType
    form_class = PaymentTypeForm


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


class PaymentListView(ListView):
    model = Payment


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm


class PaymentDetailView(DetailView):
    model = Payment


class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm


class OrderPaymentsListView(ListView):
    model = OrderPayments


class OrderPaymentsCreateView(CreateView):
    model = OrderPayments
    form_class = OrderPaymentsForm


class OrderPaymentsDetailView(DetailView):
    model = OrderPayments


class OrderPaymentsUpdateView(UpdateView):
    model = OrderPayments
    form_class = OrderPaymentsForm

