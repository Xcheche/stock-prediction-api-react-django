from django.db import models

# Create your models here.

class Students(models.Model):
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    #---------Unique constraint on student_id and name together--------
    class Meta:
        unique_together = ('student_id', 'name')