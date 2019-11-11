from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1)
    language = models.CharField(max_length=1)
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    town = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, on_delete='cascade')
