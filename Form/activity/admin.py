from django.contrib import admin

from activity.models import Faculty, Student, Feedback
# Register your models here.

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Feedback)


