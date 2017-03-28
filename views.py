from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login')
def index(request):
    return render(request, template_name='index.html')


@login_required(login_url='/login')
def view_patient(request, patient_id):
    #context = dict
    #context['patient_id'] = patient_id
    return render(request, template_name='patients/view-patient.html')