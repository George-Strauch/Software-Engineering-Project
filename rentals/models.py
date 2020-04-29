from django.db import models
from user.models import UserProfile, Address




class Property(models.Model):
    thumbnail = models.ImageField(upload_to=None)
    property_description = models.TextField()
    posted_by = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    price_per_day = models.IntegerField()



class Reservation(models.Model):
    renter = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.IntegerField()



class Feedback(models.Model):
    rating = models.IntegerField(choices=[(i, i) for i in range(11)])
    comment = models.TextField()
    reservation = models.OneToOneField(Reservation, default=None, on_delete=models.CASCADE)


# https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
class Image(models.Model):
    Property = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=None)


