from django.db import models

# Create your models here.
class links(models.Model):
    Website_Name = models.CharField(max_length=255)
    Website_Link = models.CharField(max_length=255)

class linkk(models.Model):
    url = models.URLField()
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class heading(models.Model):
    TAG = models.CharField(max_length=10)
    TEXT = models.CharField(max_length=255)