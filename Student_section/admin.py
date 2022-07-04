from django.contrib import admin
from Student_section.models import Student_table

# Register your models here.
#admin.site.register(Student_table)
@admin.register(Student_table)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Member_IdNumber','Member_Name','Profession','membership_plan')

#admin.site.register(Student_table, StudentAdmin)

