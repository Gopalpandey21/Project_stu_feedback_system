from django.db import models

# Create your models here.
class Student(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default="unknown")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20)
    mobile = models.CharField(max_length=13)
    program = models.CharField(max_length=30)
    semester = models.CharField(max_length=20, null=True)
    dob = models.DateField(null=True)
    profilePic = models.ImageField(upload_to='static', default=True)
    loginDate = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.username)
    

class Faculty(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="unknown")   
    designation = models.CharField(max_length=50)   
    email = models.EmailField(unique=True)   
    password = models.CharField(max_length=20)   
    programme = models.CharField(max_length=50)   
    mobile = models.CharField(max_length=12) 
    pic = models.ImageField(upload_to='static', default=True) 

    def __str__(self) :
        return str(self.name)
      
class Feedback(models.Model):
    name = models.CharField(max_length=100, default="unknow")
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    rating = models.IntegerField(default=4)