from pydoc import describe
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    describe = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name