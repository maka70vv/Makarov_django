from django.db import models

# Create your models here.
class Order(models.Model):
    FOOD_CHOISES = (
        ('HAMBURGER', 'HAMBURGER'),
        ('PIZZA', 'PIZZA'),
        ('ROLS', 'ROLS'),
        ('DONNER', 'DONNER'),
        ('RAMEN', 'RAMEN'),
        ('SANDWICH', 'SANDWICH')
    )
    FAST_FOOD_CHOISES = (
        ('OAZIS', 'OAZIS'),
        ('BIR EKI', 'BIR EKI'),
        ('EKI DOS', 'EKI DOS'),
        ('IMPERIA PIZZA', 'IMPERIA PIZZA'),
        ('PAPA JOHNS', 'PAPA JOHNS'),
        ('DODO', 'DODO'),
        ('KFC', 'KFC'),
    )
    title_fast_food = models.CharField(choices=FAST_FOOD_CHOISES, max_length=100)
    name = models.CharField(max_length=100)
    quatity_food = models.CharField(null=True, max_length=2)
    number = models.CharField(max_length=13)
    address = models.CharField(max_length=60)
    choose = models.CharField(choices=FOOD_CHOISES, max_length=100)