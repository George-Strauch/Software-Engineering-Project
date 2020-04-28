from django.db import models

# ---- helper models -----------------


class Address(models.Model):
    # street = models.CharField(max_length=50)
    # zip_code = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=150)
# -------------------------------------------------