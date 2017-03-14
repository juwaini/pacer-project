from django import forms


class PatientForm(forms.Form):
    full_name = forms.CharField(label='Patient Name', max_length=100)