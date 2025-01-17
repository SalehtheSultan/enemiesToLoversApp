# profiles/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instagram = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username
