from django.db import models

# Create your models here.
class Passenger(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    rewardPoints = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'passenger'