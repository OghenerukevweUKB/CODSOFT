# Generated by Django 5.0.2 on 2024-03-08 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='discription',
            new_name='description',
        ),
    ]
