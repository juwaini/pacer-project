from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'(?P<patient_id>\d+)', views.api_patient, name='api-patient'),
]