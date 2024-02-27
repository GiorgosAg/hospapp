from django.contrib import admin
from .models import Doctor, Patient, Appointment

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'phone_number', 'address', 'specialty')

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    get_full_name.short_description = 'Full name'

admin.site.register(Doctor, DoctorAdmin)

admin.site.register(Patient)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'appointment_date')

admin.site.register(Appointment, AppointmentAdmin)
