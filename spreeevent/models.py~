from django.db import models

# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length=128, unique=True)
    startday = models.IntegerField(max_length=50)
    starttime = models.IntegerField(max_length=50)
    endtime = models.IntegerField(max_length=50)
    venue = models.CharField(max_length=300)
    alias = models.CharField(max_length=300)
    def __unicode__(self):
        return self.name




