from django.urls import path
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
