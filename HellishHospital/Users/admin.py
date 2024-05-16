from django.contrib import admin

# Register your models here.
from Users.models.specialization import Specialization
from Users.models.doctor import Doctor
from Users.models.patient import Patient

admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Patient)