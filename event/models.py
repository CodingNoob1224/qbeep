from django.db import models
from members.models import User  # Import the User model from the member app

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField
    time=models.DateTimeField()
    quota=models.IntegerField()
    last_updated=models.DateTimeField(auto_now=True)
    amount=models.IntegerField(default=0)
    
class signup(models.Model):
    event=models.OneToOneField(Event,on_delete=models.CASCADE)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    signup_time=models.DateTimeField(auto_now_add=True)
    checkin=models.BooleanField(default=False)
    checkin_time=models.DateTimeField(Null=True)
    checkout=models.BooleanField(default=False)
    checkout_time=models.DateTimeField(Null=True)
    