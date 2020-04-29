from user.models import UserProfile
from django.forms import ModelForm
from .models import *



class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('rating', 'comment')



class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ('property_description', 'address', 'price_per_day',)     # todo: upload photos



class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('start_date', 'end_date',)










