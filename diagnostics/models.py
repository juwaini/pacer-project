from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

# Create your models here.


class Diagnostic(models.Model):
    diagnostic = models.TextField()
    diagnostic_for = models.ForeignKey(Patient, on_delete='cascade')
    created_on = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete='cascade')
