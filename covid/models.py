from django.db import models


class Person(models.Model):
    Date = 'D'
    Country = 'C'
    Confirmed = 'Co'
    Recovered = 'R'
    Deaths = 'D'


    date = models.FloatField()
    country = models.CharField(max_length=100)
