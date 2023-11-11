from django.db import models

class App(models.Model):

    departement = models.CharField(max_length=20)


    class Meta:
        abstract = True


class daliytime(models.Model):
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
