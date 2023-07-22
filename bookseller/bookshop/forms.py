from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users

class UsersCreationForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ('username','first_name','last_name','email','is_staff','is_active','date_joined','nick_name', 'is_author')

class UsersChangeForm(UserChangeForm):

    class Meta:
        model = Users
        fields = ('nick_name', 'is_author','username','first_name','last_name','email','is_staff','is_active','date_joined')