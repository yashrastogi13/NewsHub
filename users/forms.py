from django import forms                           #used fot creating froms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm          #we will extend the functionality of the forms
from django.forms.widgets import PasswordInput,TextInput
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):                              
        model = CustomUser                                  
        fields = UserCreationForm.Meta.fields + ('age','email')
        

        """ 
        Our CustomUser model contains all the fields of the default User model and our
        additional age field which we set.
        
        """
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser             #using CustomUser model for UserChangeForm and UserCreationForm
        fields = UserChangeForm.Meta.fields
