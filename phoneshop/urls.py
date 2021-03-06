"""dj110 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.defaults import page_not_found
from rest_framework.routers import DefaultRouter
from catalog.views import BrandViewSet


router = DefaultRouter()
router.register(r'brand', BrandViewSet)


urlpatterns = i18n_patterns(
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^logistic/', include('logistic.urls')),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^purchase/', include('purchase.urls')),
    url(r'^sales/', include('sales.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^payments/', include('payments.urls')),
    url(r'^costs/', include('costs.urls')),



    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)

handler404 = 'home.views.home'
handler500 = 'home.views.home'
handler403 = 'home.views.home'
handler400 = 'home.views.home'
