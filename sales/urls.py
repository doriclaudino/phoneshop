from django.conf.urls import url, include


from . import views


urlpatterns = (
    # urls for Seller
    url(r'^sales/seller/$', views.SellerListView.as_view(), name='sales_seller_list'),
    url(r'^sales/seller/create/$', views.SellerCreateView.as_view(),
        name='sales_seller_create'),
    url(r'^sales/seller/detail/(?P<slug>\S+)/$',
        views.SellerDetailView.as_view(), name='sales_seller_detail'),
    url(r'^sales/seller/update/(?P<slug>\S+)/$',
        views.SellerUpdateView.as_view(), name='sales_seller_update'),
)

urlpatterns += (
    # urls for SellOrderStatus
    url(r'^sales/sellorderstatus/$', views.SellOrderStatusListView.as_view(),
        name='sales_sellorderstatus_list'),
    url(r'^sales/sellorderstatus/create/$',
        views.SellOrderStatusCreateView.as_view(), name='sales_sellorderstatus_create'),
    url(r'^sales/sellorderstatus/detail/(?P<slug>\S+)/$',
        views.SellOrderStatusDetailView.as_view(), name='sales_sellorderstatus_detail'),
    url(r'^sales/sellorderstatus/update/(?P<slug>\S+)/$',
        views.SellOrderStatusUpdateView.as_view(), name='sales_sellorderstatus_update'),
)

urlpatterns += (
    # urls for SellOrder
    url(r'^sales/sellorder/$', views.SellOrderListView.as_view(),
        name='sales_sellorder_list'),
    url(r'^sales/sellorder/create/$', views.SellOrderCreateView.as_view(),
        name='sales_sellorder_create'),
    url(r'^sales/sellorder/detail/(?P<slug>\S+)/$',
        views.SellOrderDetailView.as_view(), name='sales_sellorder_detail'),
    url(r'^sales/sellorder/update/(?P<slug>\S+)/$',
        views.SellOrderUpdateView.as_view(), name='sales_sellorder_update'),
)

urlpatterns += (
    # urls for SellOrderItem
    url(r'^sales/sellorderitem/$', views.SellOrderItemListView.as_view(),
        name='sales_sellorderitem_list'),
    url(r'^sales/sellorderitem/create/$',
        views.SellOrderItemCreateView.as_view(), name='sales_sellorderitem_create'),
    url(r'^sales/sellorderitem/detail/(?P<slug>\S+)/$',
        views.SellOrderItemDetailView.as_view(), name='sales_sellorderitem_detail'),
    url(r'^sales/sellorderitem/update/(?P<slug>\S+)/$',
        views.SellOrderItemUpdateView.as_view(), name='sales_sellorderitem_update'),
)
