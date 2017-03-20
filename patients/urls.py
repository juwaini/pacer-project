from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'', views.api_patients, name='api-patients'),
]