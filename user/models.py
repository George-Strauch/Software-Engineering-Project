from django.db import models
from django.contrib.auth.models import User
from PIL import Image


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
    pfp = models.ImageField(upload_to='profile_images', null=True, blank=True, default='profile_images/default_pfp.png', verbose_name='Profile Picture')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    mid_initial = models.CharField(max_length=1, blank=True)
    dl_number = models.CharField(max_length=12, null=True, blank=True)
    address = models.ForeignKey(Address, blank=True, on_delete=models.CASCADE, null=True)
    is_landlord = models.BooleanField('Property Owner', default=False, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()  # saving image first
        img = Image.open(self.pfp.path)  # Open image using self
        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            print(self.pfp.path)
            img.save(self.pfp.path)  # saving image at the same path


    def u_save(self):
        super().save()

    def get_landlord(self):
        return self.is_landlord


    def __str__(self):
        return f'user profile for: {self.user.username}'

