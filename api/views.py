from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from api.models import Pokemon

@api_view(['GET', 'POST'])
def register(request, id: int):
    url_chain = "https://pokeapi.co/api/v2/evolution-chain/{0}/".format(id)
    r_chain = requests.get(url_chain)
    data_chain = r_chain.json()
    name = data_chain['chain']['species']['name']
    names = [name]
    pk, height, weight = get_pokemon_info(name)
    exist = Pokemon.objects.filter(id=pk)

    if len(exist) > 0:
        return Response({'message': 'Pokemon already exist'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        names.extend(get_evolutions(data_chain['chain']['evolves_to'], []))
        for name in names:
            pk, height, weight = get_pokemon_info(name)
            Pokemon.create(pk, name, height, weight)

        return Response({'message': 'pokemon has been registered'},
                        status=status.HTTP_201_CREATED)

def get_evolutions(evolves_to, names):
    if len(evolves_to) == 0:
        return names
    else:
        names.append(evolves_to[0]['species']['name'])
        return get_evolutions(evolves_to[0]['evolves_to'], names)

def get_pokemon_info(name):
    url_info = "https://pokeapi.co/api/v2/pokemon/{0}".format(name)
    r_info = requests.get(url_info)
    data_info = r_info.json()
    pk = data_info['id']
    height = data_info['height']
    weight = data_info['weight']
    return pk, height, weight