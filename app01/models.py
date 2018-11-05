from django.db import models

# Create your models here.

class user_tables(models.Model):
	name = models.CharField(max_length=32, null=True)
	pwd = models.CharField(max_length=32, null=True)
	email = models.EmailField(max_length=64, null=True)
	user_type = models.IntegerField(null=True)
	phone = models.CharField(max_length=11,null=True)
