from django.db import models

# Create your models here.

NEWLWTTER_OPTIONS = [
    ('W', 'Weekly'),
    ('M', 'Monthly')
]


class Subscription(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    options = models.CharField(
        max_length=2, choices=NEWLWTTER_OPTIONS, default='M')

    def __str__(self):
        return self.email
