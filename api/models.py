from django.contrib.gis.db import models


# Model for Pokemon description in database
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


# Model for Pokemon Evolution description in database
class Evolution(models.Model):
    PREEVOLUTION = 'preevolution'
    EVOLUTION = 'evolution'
    EVOLUTION_TYPES = [
        (PREEVOLUTION, 'Preevolution'),
        (EVOLUTION, 'Evolution')
    ]
    type = models.CharField(max_length=12, choices=EVOLUTION_TYPES, default=EVOLUTION)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    evolution = models.ForeignKey(Pokemon, related_name='evolutions', on_delete=models.CASCADE)

    @classmethod
    def create(cls, type, pokemon, evolution):
        evolution = cls(type=type, pokemon=pokemon, evolution=evolution)
        evolution.save()
        return evolution

    def __str__(self):
        return self.evolution.name + " " + self.type


# Model for Pokemon Stats description in database
class Stat(models.Model):
    type = models.CharField(max_length=18)
    pokemon = models.ForeignKey(Pokemon, related_name='stats', on_delete=models.CASCADE)
    base_stat = models.FloatField()

    @classmethod
    def create(cls, type, pokemon, base_stat):
        stat = cls(type=type, pokemon=pokemon, base_stat=base_stat)
        stat.save()
        return stat

    def __str__(self):
        return self.pokemon.name + " " + self.type + " " + self.base_stat