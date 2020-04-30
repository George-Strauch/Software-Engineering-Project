from django.db import models
from user.models import UserProfile, Address
from django.urls import reverse



class Property(models.Model):
    thumbnail = models.ImageField(upload_to='property_images', null=True)
    property_description = models.TextField(null=True)
    posted_by = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    price_per_day = models.IntegerField(null=True)

    def __str__(self):
        return self.address.street_address

    def get_absolute_url(self):
        return reverse('prop-details', kwargs={'pk': self.pk})



class Reservation(models.Model):
    renter = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return f'rented {self.property.address.street_address} from {self.start_date} until {self.end_date}'


class Feedback(models.Model):
    rating = models.IntegerField(choices=[(i, i) for i in range(11)], null=True)
    comment = models.TextField(null=True)
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, null=True)

