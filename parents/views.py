import json
from .models import Parent, Patient
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login')
def api_parents(request):
    if request.method == 'GET':
        parents = Parent.objects.all()
        retdata = []
        for parent in parents:
            data = dict()

            data['id'] = parent.id
            data['full_name'] = parent.full_name
            data['id_number'] = parent.id_number
            data['contact_number'] = parent.contact_number
            data['email'] = parent.email
            data['address'] = parent.address
            data['postcode'] = parent.postcode
            data['town'] = parent.town
            data['state'] = parent.state
            data['country'] = parent.country
            data['parent_of'] = parent.parent_of.full_name
            data['created_by'] = parent.created_by.username
            retdata.append(data)

        return JsonResponse(retdata, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)

        patient_id = data['patient_id']
        patient = Patient.objects.get(id=patient_id)

        parent = Parent()
        parent.parent_of = patient
        parent.full_name = data['full_name']
        parent.id_number = data['id_number']
        parent.contact_number = [data['contact_number']]
        parent.email = [data['email']]
        parent.address = data['address']
        parent.postcode = data['postcode']
        parent.town = data['town']
        parent.state = data['state']
        parent.country = data['country']
        parent.created_by = request.user
        parent.save()

        return HttpResponse('Successfully added parent %s' % data['full_name'])