from django.shortcuts import render

from myapp.models import Patient, Doctor, Appointment


# Create your views here.


def index(request):
    return render(request, "main.html")


def patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        history = request.POST.get('history')

        patient = Patient(
            PATIENT_NAME=name,
            PATIENT_GENDER=gender,
            PATIENT_DOB=dob,
            PATIENT_CONTACT=contact,
            PATIENT_ADDRESS=address,
            PATIENT_HISTORY=history
        )
        patient.save()
        return render(request, "main.html")
    return render(request, "patient.html")


def doctor(request):
    if request.method == 'POST':
        name = request.POST.get('doctorName')
        specialization = request.POST.get('specialization')
        contact = request.POST.get('contact')
        schedule = request.POST.get('schedule')
        unit = request.POST.get('unit')
        qualification = request.POST.get('qualification')

        doctor = Doctor(
            DOCTOR_NAME=name,
            DOCTOR_SPECIALIZATION=specialization,
            DOCTOR_CONTACT=contact,
            DOCTOR_SCHEDULE=schedule,
            DOCTOR_UNIT=unit,
            DOCTOR_QUALIFICATION=qualification
        )

        doctor.save()
        return render(request, "main.html")
    return render(request, "doctor.html")


def appointment(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patientID')
        doctor_id = request.POST.get('doctorID')
        date = request.POST.get('appointmentDate')
        status = request.POST.get('status')

        appointment = Appointment(
            PATIENT_ID=patient_id,
            DOCTOR_ID=doctor_id,
            APPOINTMENT_DATE=date,
            APPOINTMENT_STATUS=status
        )

        appointment.save()
        return render(request, "main.html")
    return render(request, "appointment.html")
