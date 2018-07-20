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
    url(r'^costs/purchasecost/$', views.CostListView.as_view(),
        name='costs_purchase_list'),
    url(r'^costs/purchasecost/create/$',
        views.CostCreateView.as_view(), name='costs_purchase_create'),
    url(r'^costs/purchasecost/detail/(?P<slug>\S+)/$',
        views.CostDetailView.as_view(), name='costs_purchase_detail'),
    url(r'^costs/purchasecost/update/(?P<slug>\S+)/$',
        views.CostUpdateView.as_view(), name='costs_purchase_update'),
)

urlpatterns += (
    # urls for ItemCost
    url(r'^costs/itemcost/$', views.CostListView.as_view(),
        name='costs_item_list'),
    url(r'^costs/itemcost/create/$', views.CostCreateView.as_view(),
        name='costs_item_create'),
    url(r'^costs/itemcost/detail/(?P<slug>\S+)/$',
        views.CostDetailView.as_view(), name='costs_item_detail'),
    url(r'^costs/itemcost/update/(?P<slug>\S+)/$',
        views.CostUpdateView.as_view(), name='costs_item_update'),
)

urlpatterns += (
    # urls for SellCost
    url(r'^costs/sellcost/$', views.CostListView.as_view(),
        name='costs_sell_list'),
    url(r'^costs/sellcost/create/$', views.CostCreateView.as_view(),
        name='costs_sell_create'),
    url(r'^costs/sellcost/detail/(?P<slug>\S+)/$',
        views.CostDetailView.as_view(), name='costs_sell_detail'),
    url(r'^costs/sellcost/update/(?P<slug>\S+)/$',
        views.CostUpdateView.as_view(), name='costs_sell_update'),
)

urlpatterns += (
    # urls for TrackingCost
    url(r'^costs/trackingcost/$', views.CostListView.as_view(),
        name='costs_tracking_list'),
    url(r'^costs/trackingcost/create/$',
        views.CostCreateView.as_view(), name='costs_tracking_create'),
    url(r'^costs/trackingcost/detail/(?P<slug>\S+)/$',
        views.CostDetailView.as_view(), name='costs_tracking_detail'),
    url(r'^costs/trackingcost/update/(?P<slug>\S+)/$',
        views.CostUpdateView.as_view(), name='costs_tracking_update'),
)
