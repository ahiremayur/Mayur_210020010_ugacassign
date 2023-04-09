from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    Roll_number= models.IntegerField()
    Department = models.CharField(max_length=100)
    Hostel= models.CharField(max_length=50)

    def __str__(self):
        return self.name