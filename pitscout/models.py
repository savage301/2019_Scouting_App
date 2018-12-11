from django.db import models

# Create your models here.
class pitscout(models.Model):
	name = models.CharField(max_length = 50)

	team_number = models.CharField(max_length = 4)

	drive_drive_type = (('Tank','Tank'),('Omni','Omni'),('Swerve','Swerve'))
	Drivetrain = models.CharField(max_length = 6, choices = drive_drive_type, default = 'Tank')

	robot_photo = models.FileField(upload_to='robot_photo/',max_length=1000,default='')