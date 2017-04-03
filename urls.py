"""pacer_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import views
from django.contrib import admin
from django.conf.urls import url, include
from patients import urls as patients_urls
from patient import urls as patient_urls
from registration import urls as registration_urls
from parents import urls as parents_urls
from diagnostics import urls as diagnostics_urls

urlpatterns = [

    # For index project
    url(r'^$', views.index, name='index'),
    url(r'^patients/(?P<patient_id>\d+)', views.patients, name='patients'),

    # For Admin
    url(r'^admin/', admin.site.urls),

    # For parents endpoint
    url(r'^api/parents', include(parents_urls.urlpatterns)),

    # For patients endpoint
    url(r'^api/patients', include(patients_urls.urlpatterns)),

    # For patient endpoint
    url(r'^api/patient', include(patient_urls.urlpatterns)),

    # For diagnostics endpoint
    url(r'^api', include(diagnostics_urls.urlpatterns)),

    # For registration endpoint
    url(r'^', include(registration_urls.urlpatterns)),
]
