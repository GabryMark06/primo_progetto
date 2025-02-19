from django.db import models
from datetime import datetime

class Corso(models.Model):
    titolo=models.CharField(max_length=50)
    descrizione=models.TextField()
    data_inizio=models.DateTimeField(default=datetime.now())
    data_fine=models.DateTimeField(default=datetime.now())
    posti_disponibili=models.IntegerField(default=0)
    

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name="Corso"
        verbose_name_plural="Corsi"
