from django.db import models

# Create your models here.


class Default(models.Model):
    first_number = models.CharField(max_length=100)
    second_number = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
