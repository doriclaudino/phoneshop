from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.templates import registration


from . import views


urlpatterns = (
    # urls for Location
    url(r'^.*', views.home, name='home'),
)
