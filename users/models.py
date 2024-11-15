from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event


User = get_user_model()

# # Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rsvped_events=models.ManyToManyField(Event, related_name='rsvped_events', blank=True)

    def __str__(self):
        return self.user.username
    