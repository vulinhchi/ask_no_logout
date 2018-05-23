from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_lenght = 50)
	password = model.CharField(max_lenght = 50)


