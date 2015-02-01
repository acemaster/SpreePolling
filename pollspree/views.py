from django.shortcuts import render

from django.http import HttpResponse
from pollspree.models import Participants
from pollspree.forms import Voteform


def index(request):
	plist=[('1','Hello'),('2','Hai')]
	if request.method == 'POST':
		form=Voteform(request.POST)
		if form.is_valid():
			c=Participants.objects.get(name=request.POST['name'])
			c.votes+=1
			c.save()	
		else:
			print form.errors
	else:
		form=Voteform()
		
	plist=Participants.objects.all()
	context_dict = {'Participants': plist, 'form': form}
	return render(request, 'pollspree/index.html',context_dict)