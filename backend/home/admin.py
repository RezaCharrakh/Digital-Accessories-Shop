from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    # Customize the UserAdmin as needed
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

# Unregister the default UserAdmin
admin.site.unregister(User)

# Register User with CustomUserAdmin
admin.site.register(User, CustomUserAdmin)


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
# admin.site.register(User)
admin.site.register(Banner)
