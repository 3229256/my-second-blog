from django.conf import settings 
from django.db import models 
from django.utils import timezone 


class Post(models.Model):
    #serve per definire la struttura del database. quando nella creazione delle cose nel database vedo autore, titolo ecc, è perche le sto creando da qua
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     title = models.CharField(max_length=200)
     text = models.TextField()
     created_date = models.DateTimeField(default=timezone.now)
     published_date = models.DateTimeField(blank=True, null=True)

     def publish(self):
         self.published_date = timezone.now() # imposta published_date alla data e ora attuale (timezone.now()) e salva il post nel database.
         self.save()

     def __str__(self):
         return self.title