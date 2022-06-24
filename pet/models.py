from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
OUR_ROLES =(
    ("Dr","doctor"),
    ("Po","pet_owner")
)
    
OUR_PETS = (
    ("Cat","cat"),
    ("Dog","dog"),
    ("Parrot","parrot"),
    ("Rabbit","Rabbit"),
    ("Guinea pig","guinea pig"),
)

class Profle(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='images')
    bio = models.CharField(max_length=100000)
    phone = models.IntegerField()
    roles = models.CharField(max_length=255,choices=OUR_ROLES)
    
    
    
class Pet(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255, blank=True, choices=OUR_PETS)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    
class Appointment(models.Model):

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    age = models.ForeignKey('Pet', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    

    
