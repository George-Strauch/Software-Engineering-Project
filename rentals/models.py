from django.db import models

class Property(models.Model):
    property_description = models.TextField()
    # posted_by = '' # todo
    address = models.TextField()
    price_per_day = models.IntegerField()



class Reservation(models.Model):
    # renter = models.ForeignKey()  todo
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.IntegerField()



class Feedback(models.Model):
    rating = models.IntegerField(choices=[(i,i) for i in range(11)])
    comment = models.TextField()
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)



# ---- helper models ----
# https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
class Image(models.Model):
    Property = models.ForeignKey(Property, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=None)
