from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from .models import Patient
from .serializers import PatientSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class PatientList(APIView):
    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)