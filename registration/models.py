from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    ADMIN = 'admin'
    DOCTOR = 'doctor'
    NURSE = 'nurse'
    PARENT = 'parent'
    PATIENT = 'patient'
    NOROLE = 'norole'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (DOCTOR, 'Doctor'),
        (NURSE, 'Nurse'),
        (PARENT, 'Parent'),
        (PATIENT, 'Patient'),
        (NOROLE, 'No Role'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    phone_number = models.TextField()
    fullname = models.TextField(max_length=150)
    role = models.CharField(choices=ROLE_CHOICES, default=NOROLE, max_length=10)
