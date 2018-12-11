from django.db import models

# Create your models here.
class matchscout(models.Model):
	name = models.CharField(max_length = 50)

	team_num = models.CharField(max_length = 4)

	alliance_colors = (('Red','Red'),('Blue','Blue'))
	alliance = models.CharField(max_length = 4, choices = alliance_colors, default = 'Red')

	score = models.IntegerField(blank = True)

	comments = models.CharField(max_length = 250)