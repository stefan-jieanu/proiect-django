# Generated by Django 4.2 on 2024-12-09 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicatie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('released', models.DateField()),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('publicatie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reviste.publicatie')),
            ],
            options={
                'verbose_name_plural': 'Filme',
            },
        ),
    ]
