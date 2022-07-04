from django.db import models


# Create your models here.
class Student_table(models.Model):
    Member_IdNumber = models.IntegerField(primary_key=True)
    Member_Name = models.CharField(max_length=50 , null=True, blank=True)
    Profession = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=40, null=True, blank=True)
    Phone_No = models.CharField(max_length=10, null=True, blank=True)
    Set_Username = models.CharField(max_length=40, null=True, blank=True)
    Set_Password = models.CharField(max_length=40, null=True, blank=True)
    membership_plan = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.Member_Name