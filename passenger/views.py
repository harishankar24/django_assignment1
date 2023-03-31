from django.shortcuts import render
from .models import Passenger
from django.db.models import Max, Min


def getPassenger(request):
    passengers = Passenger.objects.all()
    # passengers = Passenger.objects.all().values('firstName','lastName','email')
    # passengers = Passenger.objects.all().values('firstName','lastName','rewardPoints')
    # passengers = Passenger.objects.only("email")                      # didn't worked
    # passengers = Passenger.objects.all().values_list('firstName','email')              # didn't worked
    # passengers = Passenger.objects.filter(firstName__contains='a')
    # passengers = Passenger.objects.filter(lastName__endswith='ll')
    # passengers = Passenger.objects.filter(lastName__endswith='ll').filter(firstName__startswith='D')
    # passengers = Passenger.objects.all().order_by('rewardPoints')
    # passengers = Passenger.objects.all().order_by('firstName')
    # point = Passenger.objects.all().aggregate(Max('rewardPoints'))
    # print(point)
    # point = Passenger.objects.all().aggregate(Min('rewardPoints'))
    # print(point)
    return render(request, 'index.html', {'passengers':passengers})