from django.db import models
class Register(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(primary_key=True,max_length=50)
    password=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    desig=models.CharField(max_length=50,default="user")