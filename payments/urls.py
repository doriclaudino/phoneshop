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
    # urls for Payment
    url(r'^payments/salepayment/$', views.PaymentListView.as_view(),
        name='payments_salepayment_list'),
    url(r'^payments/salepayment/create/$',
        views.PaymentCreateView.as_view(), name='payments_salepayment_create'),
    url(r'^payments/salepayment/detail/(?P<slug>\S+)/$',
        views.PaymentDetailView.as_view(), name='payments_salepayment_detail'),
    url(r'^payments/salepayment/update/(?P<slug>\S+)/$',
        views.PaymentUpdateView.as_view(), name='payments_salepayment_update'),
)
