from django.db import models
from django.utils import timezone

# Create your models here.

class todo(models.Model):
    title = models.CharField(max_length=25,default='')
    text = models.TextField(max_length=100,default='')
    time = models.DateTimeField(default=timezone.now())

    

    def __str__(self):
        return self.title