from django.db import models
# Create your models here.

class words(models.Model):
    word=models.CharField(max_length=255)
    translate=models.CharField(max_length=255)
    value=models.CharField(max_length=255)

    
    




