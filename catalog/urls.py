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

urlpatterns += (
    # urls for Product
    url(r'^catalog/product/$', views.ProductListView.as_view(),
        name='catalog_product_list'),
    url(r'^catalog/product/create/$', views.ProductCreateView.as_view(),
        name='catalog_product_create'),
    url(r'^catalog/product/detail/(?P<slug>\S+)/$',
        views.ProductDetailView.as_view(), name='catalog_product_detail'),
    url(r'^catalog/product/update/(?P<slug>\S+)/$',
        views.ProductUpdateView.as_view(), name='catalog_product_update'),
)


urlpatterns += (
    # urls for ProductModel
    url(r'^catalog/productmodel/$', views.ProductModelListView.as_view(),
        name='catalog_productmodel_list'),
    url(r'^catalog/productmodel/create/$',
        views.ProductModelCreateView.as_view(), name='catalog_productmodel_create'),
    url(r'^catalog/productmodel/detail/(?P<slug>\S+)/$',
        views.ProductModelDetailView.as_view(), name='catalog_productmodel_detail'),
    url(r'^catalog/productmodel/update/(?P<slug>\S+)/$',
        views.ProductModelUpdateView.as_view(), name='catalog_productmodel_update'),
)
