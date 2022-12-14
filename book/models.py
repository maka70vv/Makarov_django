from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=60)
    description = models.TextField()
    image=models.ImageField(upload_to='')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

