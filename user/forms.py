from django.contrib.auth.models import User
from rentals.models import Address
from rentals.forms import *
from django.forms import ModelForm
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
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',  'email')



class MakeProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mid_initial', 'dl_number', 'address', 'is_landlord')   # todo: upload pfp?



class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mid_initial', 'dl_number', 'address')   # todo: upload pfp?






















