from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import IdentifierType, LocalType, Local, Identifier, Item
from .forms import IdentifierTypeForm, LocalTypeForm, LocalForm, IdentifierForm, ItemForm


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


class LocalTypeListView(ListView):
    model = LocalType


class LocalTypeCreateView(CreateView):
    model = LocalType
    form_class = LocalTypeForm


class LocalTypeDetailView(DetailView):
    model = LocalType


class LocalTypeUpdateView(UpdateView):
    model = LocalType
    form_class = LocalTypeForm


class LocalListView(ListView):
    model = Local


class LocalCreateView(CreateView):
    model = Local
    form_class = LocalForm


class LocalDetailView(DetailView):
    model = Local


class LocalUpdateView(UpdateView):
    model = Local
    form_class = LocalForm


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

