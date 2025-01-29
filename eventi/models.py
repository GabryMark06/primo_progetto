from django.db import models
from datetime import datetime

class Evento(models.Model):
    titolo=models.CharField(max_length=20)
    data_evento=models.DateTimeField(default=datetime.now())
    descrizione=models.TextField()
    partecipanti=models.IntegerField(default=0)
    

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name="Evento"
        verbose_name_plural="Eventi"

# Create your models here.
