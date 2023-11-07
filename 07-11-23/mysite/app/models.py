from django.db import models

# Create your models here.
class Profile(models.Model):
    p_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Student(models.Model):
    student_name = models.CharField(max_length=50)
