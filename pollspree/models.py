from django.db import models

class Participants(models.Model):
	name=models.CharField(max_length=128, unique=True)
	votes=models.IntegerField(default=0)
	def __unicode__(self):
		return self.name


class Voters(models.Model):
	tokenid=models.IntegerField(unique=True)
	def __unicode__(self):
		return self.tokenid


	