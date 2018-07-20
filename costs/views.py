from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import CostType, Cost
from .forms import CostTypeForm, CostForm


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
