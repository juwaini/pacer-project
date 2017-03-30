import json
from datetime import datetime
from patients.models import Patient
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def api_patient(request, patient_id):
    if request.method == 'GET':
        patient = Patient.objects.get(id=patient_id)
        retdata = dict()

        retdata['id'] = patient.id
        retdata['full_name'] = patient.full_name
        retdata['id_number'] = patient.id_number
        retdata['date_of_birth'] = patient.date_of_birth
        retdata['sex'] = patient.sex
        retdata['language'] = patient.language
        retdata['address'] = patient.address
        retdata['postcode'] = patient.postcode
        retdata['town'] = patient.town
        retdata['state'] = patient.state
        retdata['country'] = patient.country
        retdata['created_by'] = patient.created_by.username

        return JsonResponse(retdata, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        dob = data['date_of_birth'].split('T')[0]

        patient = Patient()
        patient.full_name = data['full_name']
        patient.id_number = data['id_number']
        patient.date_of_birth = datetime.strptime(dob, '%Y-%m-%d')
        patient.sex = data['sex']
        patient.language = data['language']
        patient.address = data['address']
        patient.postcode = data['postcode']
        patient.town = data['town']
        patient.state = data['state']
        patient.country = data['country']
        patient.created_by = request.user
        patient.save()

        return HttpResponse('Successfully added patient %s' % data['full_name'])