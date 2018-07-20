from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import PaymentMethod, PaymentStatus, Payment
from .forms import PaymentMethodForm, PaymentStatusForm, PaymentForm


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
