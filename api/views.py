from rest_framework.response import Response
from rest_framework import status
from api.models import Pokemon, Evolution
from api.serializers import PokemonSerializer
from rest_framework.views import APIView


class GetPokemon(APIView):
    pokemon_serializer = PokemonSerializer

    def get(self, request, pokemon_name):
        try:
            pokemon = Pokemon.objects.get(name=pokemon_name.lower())
            response = self.pokemon_serializer(pokemon, many=False)
            return Response(response.data, status=status.HTTP_200_OK)
        except Pokemon.DoesNotExist:
            message = 'Pokemon with name {0} does not exist'.format(pokemon_name)
            return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)


get_pokemon = GetPokemon.as_view()

