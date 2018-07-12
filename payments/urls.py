from django.conf.urls import url, include


from . import views


urlpatterns = (
    # urls for PaymentType
    url(r'^payments/paymenttype/$', views.PaymentTypeListView.as_view(),
        name='payments_paymenttype_list'),
    url(r'^payments/paymenttype/create/$',
        views.PaymentTypeCreateView.as_view(), name='payments_paymenttype_create'),
    url(r'^payments/paymenttype/detail/(?P<slug>\S+)/$',
        views.PaymentTypeDetailView.as_view(), name='payments_paymenttype_detail'),
    url(r'^payments/paymenttype/update/(?P<slug>\S+)/$',
        views.PaymentTypeUpdateView.as_view(), name='payments_paymenttype_update'),
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
    # urls for Payment
    url(r'^payments/payment/$', views.PaymentListView.as_view(),
        name='payments_payment_list'),
    url(r'^payments/payment/create/$', views.PaymentCreateView.as_view(),
        name='payments_payment_create'),
    url(r'^payments/payment/detail/(?P<slug>\S+)/$',
        views.PaymentDetailView.as_view(), name='payments_payment_detail'),
    url(r'^payments/payment/update/(?P<slug>\S+)/$',
        views.PaymentUpdateView.as_view(), name='payments_payment_update'),
)

urlpatterns += (
    # urls for OrderPayments
    url(r'^payments/orderpayments/$', views.OrderPaymentsListView.as_view(),
        name='payments_orderpayments_list'),
    url(r'^payments/orderpayments/create/$',
        views.OrderPaymentsCreateView.as_view(), name='payments_orderpayments_create'),
    url(r'^payments/orderpayments/detail/(?P<slug>\S+)/$',
        views.OrderPaymentsDetailView.as_view(), name='payments_orderpayments_detail'),
    url(r'^payments/orderpayments/update/(?P<slug>\S+)/$',
        views.OrderPaymentsUpdateView.as_view(), name='payments_orderpayments_update'),
)
