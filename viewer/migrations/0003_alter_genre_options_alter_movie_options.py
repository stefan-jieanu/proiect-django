# Generated by Django 4.2 on 2024-12-09 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_movie'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name_plural': 'Genuri de filme'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name_plural': 'Filme'},
        ),
    ]
