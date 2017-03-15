from . import views
from django.conf.urls import url
# from django.contrib.auth import views
from . import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
]