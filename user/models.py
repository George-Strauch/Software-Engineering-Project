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

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        mid_inital = self.cleaned_data['mid_initial']           # some of these may not be needed

        if commit:
            user.save()
        return user


