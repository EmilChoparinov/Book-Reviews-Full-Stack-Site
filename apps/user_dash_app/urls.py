from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<u_id>)', views.showUser)
]