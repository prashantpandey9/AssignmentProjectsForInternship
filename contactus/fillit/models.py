from django.db import models
from django.db import models
from datetime import datetime   
# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=100)
    mail=models.EmailField()
    message= models.TextField()
    subject=models.CharField(max_length=150)
    query=models.CharField(max_length=150)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
class Question(models.Model):
    que=models.CharField(max_length=500)
    choice1=models.CharField(max_length=500)
    choice2=models.CharField(max_length=500)
    choice3=models.CharField(max_length=500)
    choice4=models.CharField(max_length=500)
    
