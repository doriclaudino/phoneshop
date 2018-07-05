from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Location, Carrier, TrackingStatus, Tracking
from .forms import LocationForm, CarrierForm, TrackingStatusForm, TrackingForm


class LocationListView(ListView):
    model = Location


class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm


class LocationDetailView(DetailView):
    model = Location


class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm


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
