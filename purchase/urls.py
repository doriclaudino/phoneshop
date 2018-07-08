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

urlpatterns += (
    # urls for PurchaseOrderStatus
    url(r'^purchase/purchaseorderstatus/$', views.PurchaseOrderStatusListView.as_view(),
        name='purchase_purchaseorderstatus_list'),
    url(r'^purchase/purchaseorderstatus/create/$',
        views.PurchaseOrderStatusCreateView.as_view(), name='purchase_purchaseorderstatus_create'),
    url(r'^purchase/purchaseorderstatus/detail/(?P<slug>\S+)/$',
        views.PurchaseOrderStatusDetailView.as_view(), name='purchase_purchaseorderstatus_detail'),
    url(r'^purchase/purchaseorderstatus/update/(?P<slug>\S+)/$',
        views.PurchaseOrderStatusUpdateView.as_view(), name='purchase_purchaseorderstatus_update'),
)

urlpatterns += (
    # urls for PurchaseOrder
    url(r'^purchase/purchaseorder/$', views.PurchaseOrderListView.as_view(),
        name='purchase_purchaseorder_list'),
    url(r'^purchase/purchaseorder/create/$',
        views.PurchaseOrderCreateView.as_view(), name='purchase_purchaseorder_create'),
    url(r'^purchase/purchaseorder/detail/(?P<slug>\S+)/$',
        views.PurchaseOrderDetailView.as_view(), name='purchase_purchaseorder_detail'),
    url(r'^purchase/purchaseorder/update/(?P<slug>\S+)/$',
        views.PurchaseOrderUpdateView.as_view(), name='purchase_purchaseorder_update'),
)

urlpatterns += (
    # urls for PurchaseOrderItem
    url(r'^purchase/purchaseorderitem/$', views.PurchaseOrderItemListView.as_view(),
        name='purchase_purchaseorderitem_list'),
    url(r'^purchase/purchaseorderitem/create/$',
        views.PurchaseOrderItemCreateView.as_view(), name='purchase_purchaseorderitem_create'),
    url(r'^purchase/purchaseorderitem/detail/(?P<slug>\S+)/$',
        views.PurchaseOrderItemDetailView.as_view(), name='purchase_purchaseorderitem_detail'),
    url(r'^purchase/purchaseorderitem/update/(?P<slug>\S+)/$',
        views.PurchaseOrderItemUpdateView.as_view(), name='purchase_purchaseorderitem_update'),
)
