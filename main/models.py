from django.db import models

# Create your models here.


class TimeSlots(models.Model):
    user_id = models.IntegerField()
    from_stamp = models.FloatField()
    to_stamp = models.FloatField()