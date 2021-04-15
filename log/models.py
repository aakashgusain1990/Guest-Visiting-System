from django.db import models

# Create your models here.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	uname = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	gender = models.CharField(max_length=30,default='Female')
	date_field = models.DateField()
	password = models.CharField(max_length=30)

class Security_db(models.Model):
	id = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	uname = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	gender = models.CharField(max_length=30,default='Female')
	date_field = models.DateField()
	password = models.CharField(max_length=30)

class Faculty_db(models.Model):
	id = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	uname = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=30)

class Details_db(models.Model):
	id = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	email = models.CharField(max_length=30)

class Appointments_db(models.Model):
	id = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	fullname_of_visitor =models.CharField(max_length=30)
	purpose = models.CharField(max_length=50) 
	date_ofapp = models.DateTimeField()

	
	