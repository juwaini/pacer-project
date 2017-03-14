from django.db import models

# Create your models here.


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1)
    parent_name = models.CharField(max_length=100)
    language = models.CharField(max_length=1)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    town = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
