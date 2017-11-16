from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.default),
    url(r'^add$', views.add_book),
    url(r'^add/process$', views.add_book_process),
    url(r'^review_process$', views.review_process),
    url(r'^(?P<b_id>\d+)$', views.viewBook)
]