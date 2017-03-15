from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
]