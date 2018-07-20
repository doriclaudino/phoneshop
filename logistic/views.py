from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Carrier, TrackingStatus, Tracking
from .forms import CarrierForm, TrackingStatusForm, TrackingForm


class CarrierListView(ListView):
    model = Carrier


class CarrierCreateView(CreateView):
    model = Carrier
    form_class = CarrierForm


class CarrierDetailView(DetailView):
    model = Carrier


class CarrierUpdateView(UpdateView):
    model = Carrier
    form_class = CarrierForm


class TrackingStatusListView(ListView):
    model = TrackingStatus


class TrackingStatusCreateView(CreateView):
    model = TrackingStatus
    form_class = TrackingStatusForm


class TrackingStatusDetailView(DetailView):
    model = TrackingStatus


class TrackingStatusUpdateView(UpdateView):
    model = TrackingStatus
    form_class = TrackingStatusForm


class TrackingListView(ListView):
    model = Tracking


class TrackingCreateView(CreateView):
    model = Tracking
    form_class = TrackingForm


class TrackingDetailView(DetailView):
    model = Tracking


class TrackingUpdateView(UpdateView):
    model = Tracking
    form_class = TrackingForm
