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
    add_event(name="General Quiz",day=1,stime=9,endtime=12,place='NSH',alias='generalquiz')
    add_event(name="World Quiz",day=28,stime=9,endtime=12,place='ECE Seminar Hall',alias='worldquiz')
    add_event(name="Entertainment Quiz",day=27,stime=14,endtime=17,place='ECE Seminar Hall',alias='entertainmentquiz')
    add_event(name="Be A Teacher",day=27,stime=9,endtime=17,place='Near Nescafe',alias='#')
    add_event(name="Be A Teacher",day=28,stime=9,endtime=17,place='Near Nescafe',alias='#')
    add_event(name="Be A Teacher",day=1,stime=9,endtime=17,place='Near Nescafe',alias='#')
    add_event(name="OneStage",day=28,stime=15,endtime=18,place='Auditorium',alias='#')
    add_event(name="Egg Drop Blues",day=27,stime=14,endtime=17,place='Above Chemistry Dept',alias='eggdropblues')
    add_event(name="Fector",day=28,stime=10,endtime=13,place='NAB E101 & E103',alias='fector')
    add_event(name="Fector",day=1,stime=10,endtime=13,place='NAB E101 & E103',alias='fector')
    add_event(name="Amazing Race",day=1,stime=9,endtime=12,place='NAB foyer',alias='amazingrace')
    add_event(name="Jodi No 1",day=28,stime=14,endtime=17,place='NAB E101 & E103',alias='jodino1')
    add_event(name="Jodi No 1",day=1,stime=9,endtime=12,place='NAB E101 & E103',alias='jodino1')
    add_event(name="Comic Art",day=27,stime=14,endtime=17,place='EG Hall',alias='comicart')
    add_event(name="Comic Art",day=28,stime=14,endtime=17,place='EG Hall',alias='comicart')
    add_event(name="Food Fiesta",day=27,stime=9,endtime=17,place='Between NSH and NCH',alias='foodfiesta')
    add_event(name="Naithika",day=28,stime=9,endtime=12,place='NAB E104 and E103',alias='naithika')
    add_event(name="Naithika",day=1,stime=9,endtime=12,place='NAB E103',alias='naithika')
    add_event(name="Stock Bucks",day=28,stime=9,endtime=12,place='NAB E201',alias='stockbucks')
    add_event(name="Stock Bucks",day=1,stime=9,endtime=12,place='NAB E201',alias='stockbucks')
    add_event(name="Trash Morphing",day=28,stime=13,endtime=17,place='NAB Foyer',alias='trashmorphing')
    add_event(name="Ethical Hacking Workshop",day=28,stime=9,endtime=16,place='C301',alias='#')
    add_event(name="Ethical Hacking Workshop",day=1,stime=9,endtime=16,place='C301',alias='#')
    add_event(name="Big Data Workshop",day=28,stime=9,endtime=16,place='C302',alias='#')
    add_event(name="Big Data Workshop",day=1,stime=9,endtime=16,place='C302',alias='#')
    add_event(name="Digital Marketing Workshop",day=28,stime=9,endtime=16,place='C303',alias='#')
    add_event(name="Digital Marketing Workshop",day=1,stime=9,endtime=16,place='C303',alias='#')
    add_event(name="Contemprary Dance Workshop",day=28,stime=9,endtime=12,place='Above NCH',alias='#')
    add_event(name="Band Generation and Music Production Workshop",day=1,stime=9,endtime=12,place='NCH',alias='#')
    add_event(name="Canon DSLR Workshop",day=28,stime=9,endtime=16,place='NCH',alias='#')
    add_event(name="Short Film Making Workshop",day=27,stime=12,endtime=16,place='NCH',alias='#')
    add_event(name="Google Entrepreneurship Workshop",day=28,stime=14,endtime=17,place='NSH',alias='#')











for p in Participants.objects.all():
    print p
for e in Events.objects.all():
    print e

def add_part(name,votes=0):
    p=Participants.objects.get_or_create(name=name,votes=votes)
    return p

def add_event(name,day,stime,endtime,place,alias):
    p=Events.objects.get_or_create(name=name,startday=day,starttime=stime,endtime=endtime,venue=place,alias=alias)


if __name__=='__main__':
    print 'Starting pollspree population script'
    populate2()
