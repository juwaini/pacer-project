from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'diagnostics', views.api_diagnostics, name='api-diagnostics'),
]