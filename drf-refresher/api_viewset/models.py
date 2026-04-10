from django.db import models

# Create your models here.

class Doctors(models.Model):
    doctor_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    #---------Unique constraint on doctor_id and name together--------
    class Meta:
        unique_together = ('doctor_id', 'name')