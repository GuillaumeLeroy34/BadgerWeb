# Generated by Django 5.0.1 on 2024-04-05 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionId', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Etudiant',
            new_name='User',
        ),
    ]
