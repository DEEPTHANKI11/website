from django.db import models
# Create your models here.
# models.py
class Person(models.Model):
    
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    email=models.EmailField( max_length=254)
    message=models.CharField(max_length=300)

    def __str__(self):
        return self.name
    