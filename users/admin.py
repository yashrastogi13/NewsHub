from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):              #creating custom_user_admin by extending uer_admin
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','age','is_staff']

admin.site.register(CustomUser,CustomUserAdmin)

