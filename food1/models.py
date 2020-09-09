from django.db import models

# Create your models here.

class Cake(models.Model):
    image = models.ImageField(upload_to="pics")        
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

class Ice_cream(models.Model):
    image = models.ImageField(upload_to="pics")        
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

class Chocolate(models.Model):
    image = models.ImageField(upload_to="pics")        
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

class Sweets(models.Model):
    image = models.ImageField(upload_to="pics")        
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

class Cont(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()
