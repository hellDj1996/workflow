from django.db import models
import uuid

class BaseModel(models.Model):
    creator = models.CharField('creator', max_length=50)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    class Meta: 
        abstract = True 