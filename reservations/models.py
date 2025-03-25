from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reservation (models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"
# Model for booking table  
class Booking (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.IntegerField() 

    def __str__(self):
        return f"{self.user.username}'s booking on {self.date} at {self.time}"