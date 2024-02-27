from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, default=None, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, null=True, default=None)
    last_name = models.CharField(max_length=40, null=True, default=None)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    specialty = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Patient(models.Model):
    user = models.OneToOneField(User, null=True, default=None, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, null=True, default=None)
    last_name = models.CharField(max_length=40, null=True, default=None)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    allergies = models.TextField(blank=True)
    date_of_birth = models.DateField()
    insurance_provider = models.CharField(max_length=50)
    insurance_id = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,null=True, default=None, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,null=True, default=None, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    description=models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.patient}"