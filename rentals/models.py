from django.db import models
from user.models import UserProfile, User, Address
from django.urls import reverse
from PIL import Image



class Property(models.Model):
    thumbnail = models.ImageField(upload_to='property_images', null=True, blank=True)
    property_description = models.TextField(null=True)
    posted_by = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    price_per_day = models.IntegerField(null=True)

    def __str__(self):
        return self.address.street_address


    def get_absolute_url(self):
        return reverse('prop-details', kwargs={'pk': self.pk})

    def u_save(self):
        super().save()  # saving image first

        if self.thumbnail:
            img = Image.open(self.thumbnail.path)  # Open image using self
            if img.height > 300 or img.width > 300:
                new_img = (300, 300)
                img.thumbnail(new_img)
                img.save(self.thumbnail.path)  # saving image at the same path

        else:
            self.thumbnail = 'property_images/default.png'


    def x_save(self):
        super().save()  # saving image first


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()  # saving image first

        if self.thumbnail:
            img = Image.open(self.thumbnail.path)  # Open image using self
            if img.height > 300 or img.width > 300:
                new_img = (300, 300)
                img.thumbnail(new_img)
                img.save(self.thumbnail.path)  # saving image at the same path

        else:
            self.thumbnail = 'property_images/default.png'




class Reservation(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(null=True, help_text="<em>YYYY-MM-DD</em>.")
    end_date = models.DateField(null=True, help_text="<em>YYYY-MM-DD</em>.")

    def __str__(self):
        return f'rented {self.property.address.street_address} from {self.start_date} until {self.end_date}'


class Feedback(models.Model):
    rating = models.IntegerField(choices=[(i, i) for i in range(11)], null=True)
    comment = models.TextField(null=True)
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, null=True)

