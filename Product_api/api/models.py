from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20,null = False, blank = False)
    category = models.CharField(max_length=30,null = False, blank = False)
    price = models.IntegerField(null=False)
    description = models.TextField()
    stars =models.IntegerField()

    def __str__(self):
        return self.name