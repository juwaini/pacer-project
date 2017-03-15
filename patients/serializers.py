from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id',
                  'full_name',
                  'date_of_birth',
                  'sex',
                  'parent_name',
                  'language',
                  'contact_number',
                  'email',
                  'address',
                  'postcode',
                  'town',
                  'state',
                  'country')
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}