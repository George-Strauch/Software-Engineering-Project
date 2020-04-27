# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import *
# # https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9
#
#
# @receiver(post_save, sender=Property)
# def create_property_posting(sender, instance, created, **kwargs):
#     if created:
#         Property.objects.create(Proper2=instance)
#
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.save()
