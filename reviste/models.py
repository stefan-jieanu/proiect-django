from django.db import models
from django.db.models import *


# Create your models here.
class Publicatie(models.Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Revista(models.Model):
    title = CharField(max_length=128)
    description = TextField()
    publicatie = ForeignKey(Publicatie, on_delete=DO_NOTHING)
    released = DateField()
    price = IntegerField()
    rating = IntegerField()

    def __str__(self):
        return f'Titlul filmului este: {self.title}'