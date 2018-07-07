from django.conf.urls import url, include

from . import views


urlpatterns = (
    # urls for Brand
    url(r'^catalog/brand/$', views.BrandListView.as_view(),
        name='catalog_brand_list'),
    url(r'^catalog/brand/create/$', views.BrandCreateView.as_view(),
        name='catalog_brand_create'),
    url(r'^catalog/brand/detail/(?P<slug>\S+)/$',
        views.BrandDetailView.as_view(), name='catalog_brand_detail'),
    url(r'^catalog/brand/update/(?P<slug>\S+)/$',
        views.BrandUpdateView.as_view(), name='catalog_brand_update'),
)

urlpatterns += (
    # urls for Model
    url(r'^catalog/model/$', views.ModelListView.as_view(),
        name='catalog_model_list'),
    url(r'^catalog/model/create/$', views.ModelCreateView.as_view(),
        name='catalog_model_create'),
    url(r'^catalog/model/detail/(?P<slug>\S+)/$',
        views.ModelDetailView.as_view(), name='catalog_model_detail'),
    url(r'^catalog/model/update/(?P<slug>\S+)/$',
        views.ModelUpdateView.as_view(), name='catalog_model_update'),
)
