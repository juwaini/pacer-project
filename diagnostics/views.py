import json
from datetime import datetime
from .models import Diagnostic
from patients.models import Patient
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def api_diagnostics(request):
    if request.method == 'GET':
        diagnostics = Diagnostic.objects.all()
        retdata = []

        for diagnostic in diagnostics:
            data = dict()
            data['id'] = diagnostic.id
            data['diagnostic'] = diagnostic.diagnostic
            data['diagnostic_for'] = diagnostic.diagnostic_for.id
            data['created_by'] = diagnostic.created_by.id
            data['created_on'] = diagnostic.created_on
            retdata.append(data)

        return JsonResponse(retdata, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        diagnostic = Diagnostic()

        patient = Patient.objects.get(id=int(data['patient_id']))
        diagnostic.diagnostic = data['diagnostic']
        diagnostic.diagnostic_for = patient
        diagnostic.created_by = request.user
        diagnostic.created_on = datetime.now()
        diagnostic.save()

        return HttpResponse(f'Successfully added diagnostics for patient {patient.full_name}')