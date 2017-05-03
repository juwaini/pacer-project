from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'postcode/(?P<postcode>\d+)', views.api_postcode, name='api-postcode'),
]