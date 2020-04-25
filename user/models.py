from django.db import models
from django.contrib.auth.models import User
from rentals.models import Address




"""
the Django user model already has fields for:
username, password, email, first_name, last_name
"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mid_initial = models.CharField(max_length=1)
    dl_number = models.CharField(max_length=12)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_landlord = models.BooleanField(default=False)


    def __str__(self):
        return f'user profile for: {self.user.username}'

    def save(self):
        super().save()


