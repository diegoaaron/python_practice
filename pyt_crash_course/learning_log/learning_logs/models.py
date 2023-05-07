from django.db import models

# Create your models here.
class Topic(models.Model):
    """Lo que esta aprendiendo el usuario"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna una cadena que representa al objeto del modelo"""
        return self.text