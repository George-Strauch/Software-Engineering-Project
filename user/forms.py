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








class MakeProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        label=("First name"),
        max_length=30,
        widget=forms.TextInput(attrs={'autocomplete': 'first-name'}),
    )

    last_name = forms.CharField(
        label=("Last name"),
        max_length=150,
        widget=forms.TextInput(attrs={'autocomplete': 'last-name'}),
    )

    email = forms.EmailField()
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'mid_initial', 'dl_number', 'is_landlord')   # todo: upload pfp?










# class UpdateProfileForm(ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('first_name', 'last_name',  'email', 'username', 'first_name', 'last_name', 'password')






















