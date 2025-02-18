from django.db import models

# Create your models here.
class Student(models.Model):
    photo = models.ImageField(upload_to='student_images/')
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    class_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.name
