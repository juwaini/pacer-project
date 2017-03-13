from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from .forms import PatientForm
# Create your views here.


def index(request):
    return render(request, template_name='index.html')


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = PatientForm()
        return render(request, template_name='form.html', context={'form': form})