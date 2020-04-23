from django.db import models
from user.models import Basic_User, Landlord
from django import forms
from django.contrib.auth.forms import UserCreationForm


# ---- helper models -----------------
# https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
class Image(models.Model):
    Property = models.ForeignKey(Property, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=None)



class Address(models.Model):
    # street = models.CharField(max_length=50)
    # zip_code = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
# -------------------------------------------------



class Property(models.Model):
    property_description = models.TextField()
    posted_by = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    price_per_day = models.IntegerField()



class Reservation(models.Model):
    renter = models.ForeignKey(Basic_User, models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.IntegerField()



class Feedback(models.Model):
    rating = models.IntegerField(choices=[(i, i) for i in range(11)])
    comment = models.TextField()
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)



class AddressCreationForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['country', 'state', 'city', 'street address']


class FeedbackCreationForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']
