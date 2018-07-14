from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import CostType, PurchaseCost, ItemCost, SellCost, TrackingCost
from .forms import CostTypeForm, PurchaseCostForm, ItemCostForm, SellCostForm, TrackingCostForm


class CostTypeListView(ListView):
    model = CostType


class CostTypeCreateView(CreateView):
    model = CostType
    form_class = CostTypeForm


class CostTypeDetailView(DetailView):
    model = CostType


class CostTypeUpdateView(UpdateView):
    model = CostType
    form_class = CostTypeForm


class PurchaseCostListView(ListView):
    model = PurchaseCost


class PurchaseCostCreateView(CreateView):
    model = PurchaseCost
    form_class = PurchaseCostForm


class PurchaseCostDetailView(DetailView):
    model = PurchaseCost


class PurchaseCostUpdateView(UpdateView):
    model = PurchaseCost
    form_class = PurchaseCostForm


class ItemCostListView(ListView):
    model = ItemCost


class ItemCostCreateView(CreateView):
    model = ItemCost
    form_class = ItemCostForm


class ItemCostDetailView(DetailView):
    model = ItemCost


class ItemCostUpdateView(UpdateView):
    model = ItemCost
    form_class = ItemCostForm


class SellCostListView(ListView):
    model = SellCost


class SellCostCreateView(CreateView):
    model = SellCost
    form_class = SellCostForm


class SellCostDetailView(DetailView):
    model = SellCost


class SellCostUpdateView(UpdateView):
    model = SellCost
    form_class = SellCostForm


class TrackingCostListView(ListView):
    model = TrackingCost


class TrackingCostCreateView(CreateView):
    model = TrackingCost
    form_class = TrackingCostForm


class TrackingCostDetailView(DetailView):
    model = TrackingCost


class TrackingCostUpdateView(UpdateView):
    model = TrackingCost
    form_class = TrackingCostForm

