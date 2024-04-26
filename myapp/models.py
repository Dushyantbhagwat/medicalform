from django.db import models

# Create your models here.


class Patient(models.Model):
    PATIENT_ID = models.AutoField(primary_key=True)
    PATIENT_NAME = models.CharField(max_length=100)
    PATIENT_GENDER = models.CharField(max_length=10)
    PATIENT_DOB = models.DateField()
    PATIENT_CONTACT = models.BigIntegerField()
    PATIENT_ADDRESS = models.TextField()
    PATIENT_HISTORY = models.TextField()

    def __str__(self):
        return self.PATIENT_NAME


class Doctor(models.Model):
    DOCTOR_ID = models.AutoField(primary_key=True)
    DOCTOR_NAME = models.CharField(max_length=100)
    DOCTOR_SPECIALIZATION = models.CharField(max_length=100)
    DOCTOR_CONTACT = models.BigIntegerField()
    DOCTOR_SCHEDULE = models.TextField()
    DOCTOR_UNIT = models.CharField(max_length=100)
    DOCTOR_QUALIFICATION = models.TextField()

    def __str__(self):
        return self.DOCTOR_NAME


class Appointment(models.Model):
    APPOINTMENT_ID = models.AutoField(primary_key=True)
    PATIENT_ID = models.CharField(max_length=100)
    DOCTOR_ID = models.CharField(max_length=100)
    APPOINTMENT_DATE = models.DateField()
    APPOINTMENT_STATUS = models.CharField(max_length=100)

    def __str__(self):
        return f"Appointment {self.APPOINTMENT_ID}"
