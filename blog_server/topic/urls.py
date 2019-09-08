from django.conf.urls import url
from .import views

urlpatterns = [
    # /v1/topics/username
    url(r'^/(?P<username>[\w]+)$', views.topics, name='topics'),
]