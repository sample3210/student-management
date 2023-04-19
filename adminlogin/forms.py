from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'address' , 'fathername','dob','gender','contact_no','class_name','remarks']
