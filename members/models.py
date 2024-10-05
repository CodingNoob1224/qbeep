from django.db import models
from event.models import Event 
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10)
    GENDER_CHOICES=[
        ("F","Female"),
        ("M","Male")
    ]
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date=models.DateField()