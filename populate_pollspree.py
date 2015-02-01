import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','polling_project.settings')

import django
django.setup()

from pollspree.models import Participants, Voters

def populate():
	add_part(name="Test1")
	add_part(name="Test2")
	add_part(name="Test3")
	add_part(name="Test4")
	add_part(name="Test5")


for p in Participants.objects.all():
	print p

def add_part(name,votes=0):
	p=Participants.objects.get_or_create(name=name,votes=votes)
	return p


if __name__=='__main__':
	print 'Starting pollspree population script'
	populate()
