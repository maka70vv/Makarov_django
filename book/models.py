from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=60)
    description = models.TextField()
    image=models.ImageField(upload_to='')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class TvShow(models.Model):
    GENRE = (
        ('HORROR', "HORROR"),
        ("ANIME", "ANIME"),
        ("COMEDY", "COMEDY"),
        ("FANTASY", "FANTASY"),
        ("ROMANTIC", "ROMANTIC"),
        ("DRAMMA", "DRAMMA")
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    quantity = models.IntegerField()
    trailer = models.URLField()
    genre =  models.CharField(choices=GENRE, max_length=100)

    def __str__(self):
        return self.title