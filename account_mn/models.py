from django.db import models

# Create your models here.
class User(models.Model):
    pair = models.CharField(max_length=70)
    session = models.CharField(max_length=100)
    pips = models.CharField(max_length=100)
    date = models.CharField(max_length=70)
    entry_time = models.CharField(max_length=70)
    comment = models.CharField(max_length=100)
    before_chart = models.CharField(max_length=100)
    after_chart = models.CharField(max_length=70)