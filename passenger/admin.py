from django.contrib import admin
from .models import Passenger


# Register your models here.
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['id','firstName','lastName','email','rewardPoints']

    
admin.site.register(Passenger, PassengerAdmin)