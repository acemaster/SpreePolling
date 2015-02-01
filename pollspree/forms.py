from django import forms
from pollspree.models import Participants

class Voteform(forms.Form):
	plist=[('1','Hello'),('2','Hai')]
	name=forms.CharField()
	class Meta:
		model=Participants
		fields=('name','votes')