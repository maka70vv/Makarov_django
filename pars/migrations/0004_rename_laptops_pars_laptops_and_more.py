# Generated by Django 4.1.2 on 2022-12-03 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pars', '0003_laptops_pars_delete_laptops'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Laptops_pars',
            new_name='Laptops',
        ),
        migrations.RenameField(
            model_name='laptops',
            old_name='link_laptop',
            new_name='link',
        ),
    ]
