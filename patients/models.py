from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1)
    parent_name = ArrayField(models.TextField(max_length=100))
    parent_email = ArrayField(models.EmailField())
    parent_contact_number = ArrayField(models.CharField(max_length=20))
    language = models.CharField(max_length=1)
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    town = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    created_by = models.ForeignKey(User)
