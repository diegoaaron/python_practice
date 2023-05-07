from django.db import models

# Create your models here.
class Topic(models.Model):
    """Lo que esta aprendiendo el usuario"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        """Retorna una cadena que representa al objeto del modelo"""
        return self.text
    

class Entry(models.Model):
    """Algo especiico para aprender"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Representa un string para el modelo"""
        return self.text[:50] + "..."
    
