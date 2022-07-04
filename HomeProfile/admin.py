from django.contrib import admin
from .models import Book_Record,IssueBook_Record

# Register your models here.
admin.site.register(Book_Record)
admin.site.register(IssueBook_Record)