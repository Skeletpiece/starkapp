from django.db import models

# Create your models here.

class Headquarters(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length = 250)
    location = models.CharField(max_length=250)
    status = models.DateTimeField(null=True)