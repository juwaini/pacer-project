from .models import Patient
from django.http import JsonResponse

# Create your views here.


def api_patients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        data = {}
        for patient in patients:
            data['full_name'] = patient.full_name

        return JsonResponse(data)

    elif request.method == 'POST':
        return None