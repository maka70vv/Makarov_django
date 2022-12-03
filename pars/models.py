from django.db import models

# Create your models here.
class Laptops(models.Model):
    link = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=6)
    image = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title