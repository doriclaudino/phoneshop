from django.conf.urls import url, include

from . import views


urlpatterns = (
    # urls for Carrier
    url(r'^carrier/$', views.CarrierListView.as_view(),
        name='logistic_carrier_list'),
    url(r'^carrier/create/$', views.CarrierCreateView.as_view(),
        name='logistic_carrier_create'),
    url(r'^carrier/detail/(?P<slug>\S+)/$',
        views.CarrierDetailView.as_view(), name='logistic_carrier_detail'),
    url(r'^carrier/update/(?P<slug>\S+)/$',
        views.CarrierUpdateView.as_view(), name='logistic_carrier_update'),
)

urlpatterns += (
    # urls for TrackingStatus
    url(r'^trackingstatus/$', views.TrackingStatusListView.as_view(),
        name='logistic_trackingstatus_list'),
    url(r'^trackingstatus/create/$',
        views.TrackingStatusCreateView.as_view(), name='logistic_trackingstatus_create'),
    url(r'^trackingstatus/detail/(?P<slug>\S+)/$',
        views.TrackingStatusDetailView.as_view(), name='logistic_trackingstatus_detail'),
    url(r'^trackingstatus/update/(?P<slug>\S+)/$',
        views.TrackingStatusUpdateView.as_view(), name='logistic_trackingstatus_update'),
)

urlpatterns += (
    # urls for Tracking
    url(r'^tracking/$', views.TrackingListView.as_view(),
        name='logistic_tracking_list'),
    url(r'^tracking/create/$', views.TrackingCreateView.as_view(),
        name='logistic_tracking_create'),
    url(r'^tracking/detail/(?P<slug>\S+)/$',
        views.TrackingDetailView.as_view(), name='logistic_tracking_detail'),
    url(r'^tracking/update/(?P<slug>\S+)/$',
        views.TrackingUpdateView.as_view(), name='logistic_tracking_update'),
)
