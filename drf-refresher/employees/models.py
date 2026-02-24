from django.db import models

# Create your models here.

#Employee sex textchoices
class EmployeeSex(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'  
#Employee race text choices

class EmployeeRace(models.TextChoices):
    ASIAN = 'AS', 'Asian'
    BLACK = 'BL', 'Black'
    WHITE = 'WH', 'White'
    HISPANIC = 'HI', 'Hispanic'
    OTHER = 'OT', 'Other'

class Employee(models.Model):

    employee_number = models.CharField(max_length=20)
    employee_name= models.CharField(max_length=100)
    employee_sex= models.CharField(max_length=1, choices=EmployeeSex.choices)
    employee_race = models.CharField(max_length=2, choices=EmployeeRace.choices)


    def __str__(self):
        return f'{self.employee_number} - {self.employee_sex} - {self.employee_race} - {self.employee_name}'