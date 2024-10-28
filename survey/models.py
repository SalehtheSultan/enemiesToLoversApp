# survey/models.py

from django.db import models
from django.contrib.auth.models import User

class SurveyResponse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Example survey fields
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], null=True, blank=True)
    looking_for = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('both', 'Both'),
    ], null=True, blank=True)
    interests = models.ManyToManyField('Interest', blank=True)
    # Add more fields as per your survey requirements

    def __str__(self):
        return f"Survey Response by {self.user.username}"

class Interest(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
