from django.db import models
from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.full_name

