from django.contrib import admin

from .models import (
    UserProfile,
    Job,
    Rating,
    Appointment
)

admin.site.register(UserProfile)
admin.site.register(Job)
admin.site.register(Rating)
admin.site.register(Appointment)