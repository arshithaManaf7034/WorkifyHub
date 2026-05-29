from django.contrib import admin
from .models import (
    UserProfile,
    Job,
    Rating,
    Appointment,
    Skill,
    JobInterest
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category'
    )

    search_fields = (
        'name',
        'category'
    )

    list_filter = (
        'category',
    )


admin.site.register(UserProfile)
admin.site.register(Job)
admin.site.register(Rating)
admin.site.register(Appointment)
admin.site.register(JobInterest)