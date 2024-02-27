from django.urls import path 
from . import views

app_name = 'hospital'

urlpatterns = [
    path('index/', views.index_view, name="index"),
    path('patients/', views.patients_view, name="patients"),
    path('doctors/', views.doctors_view, name="doctors"),
    path('appointments/', views.appointments_view, name="appointments"),
    path('add_patient/', views.add_patient, name="add_patient"),
    path('patients/delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('patients/update/<int:pk>/', views.update_patient, name='update_patient'),
    path('add_doctor/', views.add_doctor, name="add_doctor"),
    path('doctors/delete/<int:doctor_id>', views.delete_doctor, name="delete_doctor"),
    path('doctors/update/<int:pk>/', views.update_doctor, name='update_doctor'),
    path('add_appointment/', views.add_appointment, name="add_appointment"),
    path('appointments/delete/<int:appointment_id>', views.delete_appointment, name="delete_appointment"),
    path('appointments/update/<int:pk>/', views.update_appointment, name='update_appointment'),
]