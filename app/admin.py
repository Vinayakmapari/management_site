from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ['username','user_type']
    
admin.site.register(CustomUser,UserModel)

# Register your models here.



admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)