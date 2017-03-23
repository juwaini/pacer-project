import json
from .models import Patient
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def api_patients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        retdata = []
        for patient in patients:
            data = dict()

            data['full_name'] = patient.full_name
            data['date_of_birth'] = patient.date_of_birth
            data['sex'] = patient.sex
            data['parent_name'] = patient.parent_name
            data['language'] = patient.language
            data['contact_number'] = patient.parent_contact_number
            data['email'] = patient.parent_email
            data['address'] = patient.address
            data['postcode'] = patient.postcode
            data['town'] = patient.town
            data['state'] = patient.state
            data['country'] = patient.country
            data['created_by'] = patient.created_by.username
            retdata.append(data)

        return JsonResponse(retdata, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        dob = data['date_of_birth'].split('T')[0]

        patient = Patient()
        patient.full_name = data['full_name']
        patient.date_of_birth = datetime.strptime(dob, '%Y-%m-%d')
        patient.sex = data['sex']
        patient.parent_name = [data['parent_name']]
        patient.language = data['language']
        patient.parent_contact_number = [data['contact_number']]
        patient.parent_email = [data['email']]
        patient.address = data['address']
        patient.postcode = data['postcode']
        patient.town = data['town']
        patient.state = data['state']
        patient.country = data['country']
        patient.created_by = request.user
        patient.save()

        return HttpResponse('Successfully added patient %s' % data['full_name'])
