from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import CostType, Cost, PurchaseCosts, SellCosts, ItemCosts
from .forms import CostTypeForm, CostForm, PurchaseCostsForm, SellCostsForm, ItemCostsForm


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


class CostListView(ListView):
    model = Cost


class CostCreateView(CreateView):
    model = Cost
    form_class = CostForm


class CostDetailView(DetailView):
    model = Cost


class CostUpdateView(UpdateView):
    model = Cost
    form_class = CostForm


class PurchaseCostsListView(ListView):
    model = PurchaseCosts


class PurchaseCostsCreateView(CreateView):
    model = PurchaseCosts
    form_class = PurchaseCostsForm


class PurchaseCostsDetailView(DetailView):
    model = PurchaseCosts


class PurchaseCostsUpdateView(UpdateView):
    model = PurchaseCosts
    form_class = PurchaseCostsForm


class SellCostsListView(ListView):
    model = SellCosts


class SellCostsCreateView(CreateView):
    model = SellCosts
    form_class = SellCostsForm


class SellCostsDetailView(DetailView):
    model = SellCosts


class SellCostsUpdateView(UpdateView):
    model = SellCosts
    form_class = SellCostsForm


class ItemCostsListView(ListView):
    model = ItemCosts


class ItemCostsCreateView(CreateView):
    model = ItemCosts
    form_class = ItemCostsForm


class ItemCostsDetailView(DetailView):
    model = ItemCosts


class ItemCostsUpdateView(UpdateView):
    model = ItemCosts
    form_class = ItemCostsForm

