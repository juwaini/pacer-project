from django.db import models
from patients.models import Patient
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Parent(models.Model):
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=30)
    email = ArrayField(models.EmailField())
    contact_number = ArrayField(models.CharField(max_length=20))
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    town = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    parent_of = models.ForeignKey(Patient)
    created_by = models.ForeignKey(User)