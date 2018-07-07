from django.conf.urls import url, include


from . import views


urlpatterns = (
    # urls for Supplier
    url(r'^purchase/supplier/$', views.SupplierListView.as_view(),
        name='purchase_supplier_list'),
    url(r'^purchase/supplier/create/$', views.SupplierCreateView.as_view(),
        name='purchase_supplier_create'),
    url(r'^purchase/supplier/detail/(?P<slug>\S+)/$',
        views.SupplierDetailView.as_view(), name='purchase_supplier_detail'),
    url(r'^purchase/supplier/update/(?P<slug>\S+)/$',
        views.SupplierUpdateView.as_view(), name='purchase_supplier_update'),
)
