from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    fathername = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    contact_no = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20)
    remarks = models.TextField()

    def __str__(self):
        return self.name