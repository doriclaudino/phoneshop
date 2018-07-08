from django.conf.urls import url, include


from . import views


urlpatterns = (
    # urls for IdentifierType
    url(r'^inventory/identifiertype/$', views.IdentifierTypeListView.as_view(),
        name='inventory_identifiertype_list'),
    url(r'^inventory/identifiertype/create/$',
        views.IdentifierTypeCreateView.as_view(), name='inventory_identifiertype_create'),
    url(r'^inventory/identifiertype/detail/(?P<slug>\S+)/$',
        views.IdentifierTypeDetailView.as_view(), name='inventory_identifiertype_detail'),
    url(r'^inventory/identifiertype/update/(?P<slug>\S+)/$',
        views.IdentifierTypeUpdateView.as_view(), name='inventory_identifiertype_update'),
)

urlpatterns += (
    # urls for LocationType
    url(r'^inventory/locationtype/$', views.LocationTypeListView.as_view(),
        name='inventory_locationtype_list'),
    url(r'^inventory/locationtype/create/$',
        views.LocationTypeCreateView.as_view(), name='inventory_locationtype_create'),
    url(r'^inventory/locationtype/detail/(?P<slug>\S+)/$',
        views.LocationTypeDetailView.as_view(), name='inventory_locationtype_detail'),
    url(r'^inventory/locationtype/update/(?P<slug>\S+)/$',
        views.LocationTypeUpdateView.as_view(), name='inventory_locationtype_update'),
)

urlpatterns += (
    # urls for Location
    url(r'^inventory/location/$', views.LocationListView.as_view(),
        name='inventory_location_list'),
    url(r'^inventory/location/create/$',
        views.LocationCreateView.as_view(), name='inventory_location_create'),
    url(r'^inventory/location/detail/(?P<slug>\S+)/$',
        views.LocationDetailView.as_view(), name='inventory_location_detail'),
    url(r'^inventory/location/update/(?P<slug>\S+)/$',
        views.LocationUpdateView.as_view(), name='inventory_location_update'),
)

urlpatterns += (
    # urls for Identifier
    url(r'^inventory/identifier/$', views.IdentifierListView.as_view(),
        name='inventory_identifier_list'),
    url(r'^inventory/identifier/create/$',
        views.IdentifierCreateView.as_view(), name='inventory_identifier_create'),
    url(r'^inventory/identifier/detail/(?P<slug>\S+)/$',
        views.IdentifierDetailView.as_view(), name='inventory_identifier_detail'),
    url(r'^inventory/identifier/update/(?P<slug>\S+)/$',
        views.IdentifierUpdateView.as_view(), name='inventory_identifier_update'),
)

urlpatterns += (
    # urls for Item
    url(r'^inventory/item/$', views.ItemListView.as_view(),
        name='inventory_item_list'),
    url(r'^inventory/item/create/$', views.ItemCreateView.as_view(),
        name='inventory_item_create'),
    url(r'^inventory/item/detail/(?P<slug>\S+)/$',
        views.ItemDetailView.as_view(), name='inventory_item_detail'),
    url(r'^inventory/item/update/(?P<slug>\S+)/$',
        views.ItemUpdateView.as_view(), name='inventory_item_update'),
)
