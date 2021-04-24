from django.db import models
from django import forms
# Create your models here.
class info(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    auth = models.CharField(max_length=100, default=None)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class facultyt(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class securityt(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class role(models.Model):
    username = models.CharField(max_length=50,unique=True)
    roles = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class visitort(models.Model):
    GEN_CHOICES = (
        ('m','Male'),
        ('f','Female'),
        ('o','Others')
    )
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10,choices=GEN_CHOICES,default='m')
    username = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    govt_id = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.username

class appointments(models.Model):
    username = models.ForeignKey(visitort, on_delete=models.CASCADE, null=True)
    email = models.ForeignKey(facultyt, on_delete=models.CASCADE, null=True)
    doa = models.DateField()
    timeIn = models.TimeField()
    purpose = models.TextField()
    status = models.CharField(max_length=50,default= 'Pending')
    token = models.CharField(max_length=100, blank = True)
    def __str__(self):
        return self.username