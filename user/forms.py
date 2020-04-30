# from rentals.models import Address
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

# https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/


# will be coupled with Profile update, see:
# https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9
# at 3:20 in
class MakeUserForm(UserCreationForm):
    # https://stackoverflow.com/questions/5745197/django-create-custom-usercreationform
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')




# class MakeProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('is_landlord',)   # todo: upload pfp?




class MakeProfileForm(forms.Form):
    property_owner = forms.BooleanField(required=False, )
    class Meta:
        fields = ('property_owner',)



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mid_initial', 'dl_number',)   # todo: upload pfp?



class PfpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('pfp',)



class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('country', 'state', 'city', 'street_address', 'zip_code')



class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)
