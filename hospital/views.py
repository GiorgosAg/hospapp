from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment
from .forms import PatientForm, DoctorForm, AppointmentForm

def index_view(request):
    return render(request, 'index.html')

def patients_view(request):
    patients = Patient.objects.all()
    context = {'patients' : patients}
    return render(request, 'patients.html', context)

def doctors_view(request):
    doctors = Doctor.objects.all()
    context = {'doctors' : doctors}
    return render(request, 'doctors.html', context)

def appointments_view(request):
    appointments = Appointment.objects.all()
    context = {'appointments' : appointments}
    return render(request, 'appointments.html', context)

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hospital/patients/')
    else:       
        form = PatientForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name})
    context = {'form': form}
    return render(request, 'add_patient.html', context)

def delete_patient(request, patient_id):
    if request.method == 'POST':
        try:
            patient = Patient.objects.get(id=patient_id)
            patient.delete()
            return redirect('/hospital/patients/')
        except Patient.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Patient not found.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})
    
def update_patient(request, pk):
    patient = Patient.objects.get(pk=pk)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/hospital/patients/')
    else:
        form = PatientForm(instance=patient)

    context = {'form': form, 'patient': patient}
    return render(request, 'update_patient.html', context)

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hospital/doctors/')
        else:
            print(form.errors)
    else:       
        form = DoctorForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name})
    context = {'form': form}
    return render(request, 'add_doctor.html', context)

def delete_doctor(request, doctor_id):
    if request.method == 'POST':
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            doctor.delete()
            return redirect('/hospital/doctors/')
        except Doctor.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Doctor not found.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})
    
def update_doctor(request, pk):
    doctor = Doctor.objects.get(pk=pk)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('/hospital/doctors/')
    else:
        form = DoctorForm(instance=doctor)

    context = {'form': form, 'doctor': doctor}
    return render(request, 'update_doctor.html', context)

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hospital/appointments/')
    else:       
        form = AppointmentForm()
    context = {
        'form': form,
        'patients': Patient.objects.all(),
        'doctors': Doctor.objects.all()}
    return render(request, 'add_appointment.html', context)

def delete_appointment(request, appointment_id):
    if request.method == 'POST':
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            return redirect('/hospital/appointments/')
        except Appointment.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Appointment not found.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})
    
def update_appointment(request, pk):
    appointment = Appointment.objects.get(pk=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/hospital/appointments/')
    else:
        form = AppointmentForm(instance=appointment)

    context = {'form': form, 
               'appointment': appointment, 
               'patients': Patient.objects.all(),
               'doctors': Doctor.objects.all(),}
    return render(request, 'update_appointment.html', context)