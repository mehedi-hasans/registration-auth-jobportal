from django.contrib import admin
from .models import *
# Register your models here.
class Custom_User_Display(admin.ModelAdmin):
    list_display=['id','display_name','email','user_type']


admin.site.register(Custom_User,Custom_User_Display)