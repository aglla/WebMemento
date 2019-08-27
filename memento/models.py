from django.db import models

# Create your models here.

class MementoItem(models.Model):
    title = models.TextField()
    link = models.TextField()
    note = models.TextField()
    
