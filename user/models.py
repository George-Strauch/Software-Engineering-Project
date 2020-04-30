from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    zip_code = models.CharField(max_length=6, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street_address = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.street_address




"""
the Django user model already has fields for:
username, password, email, first_name, last_name
"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE, null=True)
    mid_initial = models.CharField(max_length=1, blank=True)
    dl_number = models.CharField(max_length=12, null=True, blank=True)
    address = models.ForeignKey(Address, blank=True, on_delete=models.CASCADE, null=True)
    is_landlord = models.BooleanField('Property Owner', default=False, blank=True)

    def get_landlord(self):
        return self.is_landlord


    def __str__(self):
        return f'user profile for: {self.user.username}'

