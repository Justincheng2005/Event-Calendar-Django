from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    classRel = models.CharField(max_length=200)
    description = models.TextField()
    dateTime = models.DateTimeField()
    def __str__(self):
        return f"{self.name} at {self.location} at {self.dateTime}"