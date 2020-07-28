from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=20, blank=False, default='')
    password = models.CharField(max_length=2000,blank=False, default='')

class manager(models.Model):
    userid = models.ForeignKey('user', on_delete=models.CASCADE,)
    website = models.CharField(max_length=20,blank=False, default='')
    webusername = models.CharField(max_length=20,blank=False, default='')
    webpwd = models.CharField(max_length=2000,blank=False, default='')
    
