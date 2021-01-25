from django.contrib.gis.db import models

# Model for DataSet description in database
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()

    @classmethod
    def create(cls, id, name, height, weight):
        pokemon = cls(id=id, name=name, height=height, weight=weight)
        pokemon.save()
        return pokemon

    def __str__(self):
        return self.name

class Evolution(models.Model):
    PREEVOLUTION = 'preevolution'
    EVOLUTION = 'evolution'
    EVOLUTION_TYPES = [
        (PREEVOLUTION, 'Preevolution'),
        (EVOLUTION, 'Evolution')
    ]
    type = models.CharField(max_length=12, choices=EVOLUTION_TYPES, default=EVOLUTION)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    @classmethod
    def create(cls, type, pokemon):
        evolution = cls(type=type, pokemon=pokemon)
        evolution.save()
        return evolution

    def __str__(self):
        return self.type