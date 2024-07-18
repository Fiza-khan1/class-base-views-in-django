from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('end',kwargs={'id':self.id})


