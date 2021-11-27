from django.db import models

# Create your models here.
class Contacts(models.Model):
    Name=models.CharField(max_length=10)
    Email=models.EmailField(max_length=30)
    Subject=models.CharField(max_length=200)
    Message=models.TextField(blank='True',null='True')
   
    def __str__(self):
        return self.Email
