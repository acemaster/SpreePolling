from django.shortcuts import render

from django.http import HttpResponse
from spreeevent.models import Events
import datetime


def index(request):
    plist=Events.objects.all()
    time=datetime.datetime.now()
    hour=time.hour
    day=time.day
    print time
    context_dict = {'Events': plist, 'hour': hour, 'day': day}
    return render(request, 'spreeevent/index.html',context_dict)