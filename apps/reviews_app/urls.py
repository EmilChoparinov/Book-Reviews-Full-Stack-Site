from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.default),
    url(r'^add$', views.add_book),
    url(r'^add/process$', views.add_book_process),
    url(r'^(?P<id>\d+)$', views.viewBook)
]