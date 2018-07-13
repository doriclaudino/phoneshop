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
    # urls for Cost
    url(r'^costs/cost/$', views.CostListView.as_view(), name='costs_cost_list'),
    url(r'^costs/cost/create/$', views.CostCreateView.as_view(),
        name='costs_cost_create'),
    url(r'^costs/cost/detail/(?P<slug>\S+)/$',
        views.CostDetailView.as_view(), name='costs_cost_detail'),
    url(r'^costs/cost/update/(?P<slug>\S+)/$',
        views.CostUpdateView.as_view(), name='costs_cost_update'),
)

urlpatterns += (
    # urls for PurchaseCosts
    url(r'^costs/purchasecosts/$', views.PurchaseCostsListView.as_view(),
        name='costs_purchasecosts_list'),
    url(r'^costs/purchasecosts/create/$',
        views.PurchaseCostsCreateView.as_view(), name='costs_purchasecosts_create'),
    url(r'^costs/purchasecosts/detail/(?P<slug>\S+)/$',
        views.PurchaseCostsDetailView.as_view(), name='costs_purchasecosts_detail'),
    url(r'^costs/purchasecosts/update/(?P<slug>\S+)/$',
        views.PurchaseCostsUpdateView.as_view(), name='costs_purchasecosts_update'),
)

urlpatterns += (
    # urls for SellCosts
    url(r'^costs/sellcosts/$', views.SellCostsListView.as_view(),
        name='costs_sellcosts_list'),
    url(r'^costs/sellcosts/create/$', views.SellCostsCreateView.as_view(),
        name='costs_sellcosts_create'),
    url(r'^costs/sellcosts/detail/(?P<slug>\S+)/$',
        views.SellCostsDetailView.as_view(), name='costs_sellcosts_detail'),
    url(r'^costs/sellcosts/update/(?P<slug>\S+)/$',
        views.SellCostsUpdateView.as_view(), name='costs_sellcosts_update'),
)

urlpatterns += (
    # urls for ItemCosts
    url(r'^costs/itemcosts/$', views.ItemCostsListView.as_view(),
        name='costs_itemcosts_list'),
    url(r'^costs/itemcosts/create/$', views.ItemCostsCreateView.as_view(),
        name='costs_itemcosts_create'),
    url(r'^costs/itemcosts/detail/(?P<slug>\S+)/$',
        views.ItemCostsDetailView.as_view(), name='costs_itemcosts_detail'),
    url(r'^costs/itemcosts/update/(?P<slug>\S+)/$',
        views.ItemCostsUpdateView.as_view(), name='costs_itemcosts_update'),
)


urlpatterns += (
    # urls for TrackingCosts
    url(r'^costs/trackingcosts/$', views.TrackingCostsListView.as_view(),
        name='costs_trackingcosts_list'),
    url(r'^costs/trackingcosts/create/$',
        views.TrackingCostsCreateView.as_view(), name='costs_trackingcosts_create'),
    url(r'^costs/trackingcosts/detail/(?P<slug>\S+)/$',
        views.TrackingCostsDetailView.as_view(), name='costs_trackingcosts_detail'),
    url(r'^costs/trackingcosts/update/(?P<slug>\S+)/$',
        views.TrackingCostsUpdateView.as_view(), name='costs_trackingcosts_update'),
)
