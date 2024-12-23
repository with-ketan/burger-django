from django.db import models

# Create your models here.
class AboutUs(models.Model):
    Title=models.CharField(max_length=60)
    # objective=models.TextField()
    # place=models.CharField(max_length=100)
    # email=models.CharField(max_length=60)
    # contact=models.IntegerField()
    Discraption=models.CharField(max_length=500)
 
    def __str__(self):
        return self.Title
    
class ContactUs(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10,default="phone")
    description=models.TextField()

    def __str__(self):
        return self.name
    
class Project(models.Model):
    Pimg=models.ImageField()
    Pname=models.CharField(max_length= 50)
    Pdis=models.TextField()
    rate=models.IntegerField()

    def __str__(self) -> str:
        return self.Pname