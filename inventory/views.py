from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import IdentifierType, LocationType, Location, Identifier, Item
from .forms import IdentifierTypeForm, LocationTypeForm, LocationForm, IdentifierForm, ItemForm


class IdentifierTypeListView(ListView):
    model = IdentifierType


class IdentifierTypeCreateView(CreateView):
    model = IdentifierType
    form_class = IdentifierTypeForm


class IdentifierTypeDetailView(DetailView):
    model = IdentifierType


class IdentifierTypeUpdateView(UpdateView):
    model = IdentifierType
    form_class = IdentifierTypeForm


class LocationTypeListView(ListView):
    model = LocationType


class LocationTypeCreateView(CreateView):
    model = LocationType
    form_class = LocationTypeForm


class LocationTypeDetailView(DetailView):
    model = LocationType


class LocationTypeUpdateView(UpdateView):
    model = LocationType
    form_class = LocationTypeForm


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


class IdentifierListView(ListView):
    model = Identifier


class IdentifierCreateView(CreateView):
    model = Identifier
    form_class = IdentifierForm


class IdentifierDetailView(DetailView):
    model = Identifier


class IdentifierUpdateView(UpdateView):
    model = Identifier
    form_class = IdentifierForm


class ItemListView(ListView):
    model = Item


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm


class ItemDetailView(DetailView):
    model = Item


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm

