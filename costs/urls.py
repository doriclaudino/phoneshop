from django.conf.urls import url, include


from . import views

urlpatterns = (
    # urls for CostType
    url(r'^costs/costtype/$', views.CostTypeListView.as_view(),
        name='costs_costtype_list'),
    url(r'^costs/costtype/create/$', views.CostTypeCreateView.as_view(),
        name='costs_costtype_create'),
    url(r'^costs/costtype/detail/(?P<slug>\S+)/$',
        views.CostTypeDetailView.as_view(), name='costs_costtype_detail'),
    url(r'^costs/costtype/update/(?P<slug>\S+)/$',
        views.CostTypeUpdateView.as_view(), name='costs_costtype_update'),
)

urlpatterns += (
    # urls for PurchaseCost
    url(r'^costs/purchasecost/$', views.PurchaseCostListView.as_view(),
        name='costs_purchasecost_list'),
    url(r'^costs/purchasecost/create/$',
        views.PurchaseCostCreateView.as_view(), name='costs_purchasecost_create'),
    url(r'^costs/purchasecost/detail/(?P<slug>\S+)/$',
        views.PurchaseCostDetailView.as_view(), name='costs_purchasecost_detail'),
    url(r'^costs/purchasecost/update/(?P<slug>\S+)/$',
        views.PurchaseCostUpdateView.as_view(), name='costs_purchasecost_update'),
)

urlpatterns += (
    # urls for ItemCost
    url(r'^costs/itemcost/$', views.ItemCostListView.as_view(),
        name='costs_itemcost_list'),
    url(r'^costs/itemcost/create/$', views.ItemCostCreateView.as_view(),
        name='costs_itemcost_create'),
    url(r'^costs/itemcost/detail/(?P<slug>\S+)/$',
        views.ItemCostDetailView.as_view(), name='costs_itemcost_detail'),
    url(r'^costs/itemcost/update/(?P<slug>\S+)/$',
        views.ItemCostUpdateView.as_view(), name='costs_itemcost_update'),
)

urlpatterns += (
    # urls for SellCost
    url(r'^costs/sellcost/$', views.SellCostListView.as_view(),
        name='costs_sellcost_list'),
    url(r'^costs/sellcost/create/$', views.SellCostCreateView.as_view(),
        name='costs_sellcost_create'),
    url(r'^costs/sellcost/detail/(?P<slug>\S+)/$',
        views.SellCostDetailView.as_view(), name='costs_sellcost_detail'),
    url(r'^costs/sellcost/update/(?P<slug>\S+)/$',
        views.SellCostUpdateView.as_view(), name='costs_sellcost_update'),
)

urlpatterns += (
    # urls for TrackingCost
    url(r'^costs/trackingcost/$', views.TrackingCostListView.as_view(),
        name='costs_trackingcost_list'),
    url(r'^costs/trackingcost/create/$',
        views.TrackingCostCreateView.as_view(), name='costs_trackingcost_create'),
    url(r'^costs/trackingcost/detail/(?P<slug>\S+)/$',
        views.TrackingCostDetailView.as_view(), name='costs_trackingcost_detail'),
    url(r'^costs/trackingcost/update/(?P<slug>\S+)/$',
        views.TrackingCostUpdateView.as_view(), name='costs_trackingcost_update'),
)
