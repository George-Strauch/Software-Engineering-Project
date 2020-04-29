from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User


class Address(models.Model):
    zip_code = models.CharField(max_length=6, blank=True)
    country = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50, blank=True)
    street_address = models.CharField(max_length=150, blank=True)

"""
the Django user model already has fields for:
username, password, email, first_name, last_name
"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    mid_initial = models.CharField(max_length=1, blank=True)
    dl_number = models.CharField(max_length=12)
    address = models.ForeignKey(Address, default=None, blank=True, on_delete=models.CASCADE)
    is_landlord = models.BooleanField('Property Owner', default=False, blank=True)


    def __str__(self):
        return f'user profile for: {self.user.username}'

    # def save(self, *args, **kwargs):
    #     new_user = User.objects.create(username=self.name)
