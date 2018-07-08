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
    # urls for LocalType
    url(r'^inventory/localtype/$', views.LocalTypeListView.as_view(),
        name='inventory_localtype_list'),
    url(r'^inventory/localtype/create/$',
        views.LocalTypeCreateView.as_view(), name='inventory_localtype_create'),
    url(r'^inventory/localtype/detail/(?P<slug>\S+)/$',
        views.LocalTypeDetailView.as_view(), name='inventory_localtype_detail'),
    url(r'^inventory/localtype/update/(?P<slug>\S+)/$',
        views.LocalTypeUpdateView.as_view(), name='inventory_localtype_update'),
)

urlpatterns += (
    # urls for Local
    url(r'^inventory/local/$', views.LocalListView.as_view(),
        name='inventory_local_list'),
    url(r'^inventory/local/create/$', views.LocalCreateView.as_view(),
        name='inventory_local_create'),
    url(r'^inventory/local/detail/(?P<slug>\S+)/$',
        views.LocalDetailView.as_view(), name='inventory_local_detail'),
    url(r'^inventory/local/update/(?P<slug>\S+)/$',
        views.LocalUpdateView.as_view(), name='inventory_local_update'),
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
