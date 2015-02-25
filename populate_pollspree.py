import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','polling_project.settings')

import django
django.setup()

from pollspree.models import Participants, Voters
from spreeevent.models import Events

def populate():
    add_part(name="Test1")
    add_part(name="Test2")
    add_part(name="Test3")
    add_part(name="Test4")
    add_part(name="Test5")

def populate2():
    add_event(name="Test1",day=26,stime=12,endtime=13,place='hello')
    add_event(name="Test2",day=27,stime=17,endtime=18,place='hello')
    add_event(name="Test3",day=27,stime=18,endtime=19,place='hello')
    add_event(name="Test4",day=28,stime=19,endtime=20,place='hello')




for p in Participants.objects.all():
    print p
for e in Events.objects.all():
    print e

def add_part(name,votes=0):
    p=Participants.objects.get_or_create(name=name,votes=votes)
    return p

def add_event(name,day,stime,endtime,place):
    p=Events.objects.get_or_create(name=name,startday=day,starttime=stime,endtime=endtime,venue=place)


if __name__=='__main__':
    print 'Starting pollspree population script'
    populate2()
