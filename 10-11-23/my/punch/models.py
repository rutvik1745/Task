from django.db import models

# Create your models here.
class punch1(models.Model):
    startWork = models.DateTimeField(max_length=60)
    endWork = models.DateTimeField()