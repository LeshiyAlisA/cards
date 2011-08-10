from django.db import models
# Create your models here.

class word(models.Model):
    word=models.CharField(max_length=255)
    transcription=models.CharField(max_length=255)
    value=models.CharField(max_length=255)
    id_user=models.IntegerField()   


    
    




