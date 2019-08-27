from django.db import models

# Create your models here.

class MementoItem(models.Model):
    title = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    blurb = models.TextField(blank=True, null=True)
