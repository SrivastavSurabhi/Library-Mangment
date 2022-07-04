from django import forms
from .models import Student_table



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student_table
        fields=['Member_IdNumber','Member_Name','Profession','Email','Phone_No','Set_Username','Set_Password','membership_plan']
        widgets = {
            'Member_IdNumber': forms.NumberInput( attrs={'class':'form-control'}),
            'Member_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Profession': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Phone_No': forms.NumberInput(attrs={'class': 'form-control'}),
            'Set_Username': forms.TextInput(attrs={'class': 'form-control'}),
            'Set_Password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'membership_plan': forms.TextInput(attrs={'class': 'form-control'}),

        }

