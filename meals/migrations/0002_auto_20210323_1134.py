# Generated by Django 3.1.7 on 2021-03-23 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meals',
            new_name='Meal',
        ),
    ]