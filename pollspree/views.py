from django.shortcuts import render

from django.http import HttpResponse
from pollspree.models import Participants


def index(request):
	plist=Participants.objects.all()
	context_dict = {'Participants': plist}
	return render(request, 'pollspree/index.html',context_dict)