# Generated by Django 4.1.2 on 2022-11-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_fast_food', models.CharField(choices=[('OAZIS', 'OAZIS'), ('BIR EKI', 'BIR EKI'), ('EKI DOS', 'EKI DOS'), ('IMPERIA PIZZA', 'IMPERIA PIZZA'), ('PAPA JOHNS', 'PAPA JOHNS'), ('DODO', 'DODO'), ('KFC', 'KFC')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=60)),
                ('choose', models.CharField(choices=[('HAMBURGER', 'HAMBURGER'), ('PIZZA', 'PIZZA'), ('ROLS', 'ROLS'), ('DONNER', 'DONNER'), ('RAMEN', 'RAMEN'), ('SANDWICH', 'SANDWICH')], max_length=100)),
            ],
        ),
    ]
