from django.conf.urls import url, include


from . import views


urlpatterns = (
    # urls for PaymentMethod
    url(r'^payments/paymentmethod/$', views.PaymentMethodListView.as_view(),
        name='payments_paymentmethod_list'),
    url(r'^payments/paymentmethod/create/$',
        views.PaymentMethodCreateView.as_view(), name='payments_paymentmethod_create'),
    url(r'^payments/paymentmethod/detail/(?P<slug>\S+)/$',
        views.PaymentMethodDetailView.as_view(), name='payments_paymentmethod_detail'),
    url(r'^payments/paymentmethod/update/(?P<slug>\S+)/$',
        views.PaymentMethodUpdateView.as_view(), name='payments_paymentmethod_update'),
)

urlpatterns += (
    # urls for PaymentStatus
    url(r'^payments/paymentstatus/$', views.PaymentStatusListView.as_view(),
        name='payments_paymentstatus_list'),
    url(r'^payments/paymentstatus/create/$',
        views.PaymentStatusCreateView.as_view(), name='payments_paymentstatus_create'),
    url(r'^payments/paymentstatus/detail/(?P<slug>\S+)/$',
        views.PaymentStatusDetailView.as_view(), name='payments_paymentstatus_detail'),
    url(r'^payments/paymentstatus/update/(?P<slug>\S+)/$',
        views.PaymentStatusUpdateView.as_view(), name='payments_paymentstatus_update'),
)


urlpatterns += (
    # urls for SalePayment
    url(r'^payments/salepayment/$', views.SalePaymentListView.as_view(),
        name='payments_salepayment_list'),
    url(r'^payments/salepayment/create/$',
        views.SalePaymentCreateView.as_view(), name='payments_salepayment_create'),
    url(r'^payments/salepayment/detail/(?P<slug>\S+)/$',
        views.SalePaymentDetailView.as_view(), name='payments_salepayment_detail'),
    url(r'^payments/salepayment/update/(?P<slug>\S+)/$',
        views.SalePaymentUpdateView.as_view(), name='payments_salepayment_update'),
)

urlpatterns += (
    # urls for PurchasePayment
    url(r'^payments/purchasepayment/$', views.PurchasePaymentListView.as_view(),
        name='payments_purchasepayment_list'),
    url(r'^payments/purchasepayment/create/$',
        views.PurchasePaymentCreateView.as_view(), name='payments_purchasepayment_create'),
    url(r'^payments/purchasepayment/detail/(?P<slug>\S+)/$',
        views.PurchasePaymentDetailView.as_view(), name='payments_purchasepayment_detail'),
    url(r'^payments/purchasepayment/update/(?P<slug>\S+)/$',
        views.PurchasePaymentUpdateView.as_view(), name='payments_purchasepayment_update'),
)

urlpatterns += (
    # urls for TrackingPayment
    url(r'^payments/trackingpayment/$', views.TrackingPaymentListView.as_view(),
        name='payments_trackingpayment_list'),
    url(r'^payments/trackingpayment/create/$',
        views.TrackingPaymentCreateView.as_view(), name='payments_trackingpayment_create'),
    url(r'^payments/trackingpayment/detail/(?P<slug>\S+)/$',
        views.TrackingPaymentDetailView.as_view(), name='payments_trackingpayment_detail'),
    url(r'^payments/trackingpayment/update/(?P<slug>\S+)/$',
        views.TrackingPaymentUpdateView.as_view(), name='payments_trackingpayment_update'),
)
