from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login')
def index(request):
    return render(request, template_name='index/index.html')


@login_required(login_url='/login')
def patients(request, patient_id):
    return render(request, template_name='patients/index.html')