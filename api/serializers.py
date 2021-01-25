from api.models import Pokemon, Evolution
from rest_framework.serializers import ModelSerializer


# Serializer class for Single pokemon in evolution
class SinglePokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'height', 'weight')


# Serializer class for Evolution and nested pokemon
class EvolutionSerializer(ModelSerializer):
    pokemon = SinglePokemonSerializer(many=False)

    class Meta:
        model = Evolution
        fields = ('type', 'pokemon')


# Serializer class for Pokemon and nested evolutions
class PokemonSerializer(ModelSerializer):
    evolutions = EvolutionSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'height', 'weight', 'evolutions')


