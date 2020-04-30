from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile
from .models import Address

# https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         a = Address.objects.create()
#         u = UserProfile.objects.create(user=instance, address=a)
#         u.save()



# @receiver(post_save, sender=UserProfile)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         a = Address.objects.create()
#         instance.address = a


