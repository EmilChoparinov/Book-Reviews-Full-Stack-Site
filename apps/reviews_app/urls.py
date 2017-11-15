from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.default),
    url(r'^add$', views.add),
    url(r'^(?P<id>\d+)$', views.viewBook)
]