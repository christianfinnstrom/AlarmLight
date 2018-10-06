from django.db import models

# Create your models here
class Alarm(models.Model):
    alarm_text = models.CharField(max_length=200)
    alarm_datetime = models.DateTimeField('alarm time')
