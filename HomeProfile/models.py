from django.db import models
from django.db.models.fields import DateField


# Create your models here.
class Book_Record(models.Model):
    Book_Id = models.IntegerField(primary_key=True)
    Book_Title = models.CharField(max_length=50, null=True, blank=True)
    Author_Name = models.CharField(max_length=30 ,default='Not available', null=True, blank=True)
    Catergory = models.CharField(max_length=40 , default='', null=True, blank=True)
    Quantity= models.IntegerField(default='')

    def __str__(self) :
        return (self.Book_Title)

# Create your models here.
class IssueBook_Record(models.Model):
    Member_IdNumber = models.IntegerField(primary_key=True)
    Member_Name = models.CharField(max_length = 50, null=True, blank=True)
    Book_Id = models.IntegerField(default='')
    Book_Title = models.CharField(max_length=50, null=True, blank=True)
    Issuedate = models.DateTimeField(default='')
    Expirydate = models.DateTimeField(default='')

    def __str__(self):
        return (self.Member_Name)
