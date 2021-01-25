from api.models import Evolution, Pokemon, Stat
import requests

# get_pokemon_info allows get pokemon base information by name
def get_pokemon_info(name):
    url_info = "https://pokeapi.co/api/v2/pokemon/{0}".format(name)
    r_info = requests.get(url_info)
    data_info = r_info.json()
    pk = data_info['id']
    height = data_info['height']
    weight = data_info['weight']
    stats = data_info['stats']
    return pk, height, weight, stats


# register_stats allows register 6 categories of stats by pokemon
def register_stats(pokemon, stats):
    for stat in stats:
        stat_name = stat['stat']['name']
        stat_value = stat['base_stat']
        Stat.create(stat_name, pokemon, stat_value)


# inser_evolutions allows insert all pokemon in the evolution chain and associate pre and evolution
def insert_evolutions(evolves_to, before):
    if len(evolves_to) > 0:
        for evolves in evolves_to:
            name = evolves['species']['name']
            pk, height, weight, stats = get_pokemon_info(name)
            actual = Pokemon.create(pk, name, height, weight)
            register_stats(actual, stats)
            for poke in before:
                Evolution.create(Evolution.EVOLUTION, actual, poke)
                Evolution.create(Evolution.PREEVOLUTION, poke, actual)
            if len(evolves_to) == 1:
                before.append(actual)
        if len(evolves['evolves_to']) > 0:
            return insert_evolutions(evolves['evolves_to'], before)
        else:
            return


# registe_evolution get the evolution from api and insert the firts pokemon in the chain
def register_evolution(evolution_chain_id: int):
    url_chain = "https://pokeapi.co/api/v2/evolution-chain/{0}/".format(evolution_chain_id)
    r_chain = requests.get(url_chain)
    if r_chain.status_code == 200:
        data_chain = r_chain.json()
        name = data_chain['chain']['species']['name']
        pk, height, weight, stats = get_pokemon_info(name)
        exist = Pokemon.objects.filter(id=pk)

        if len(exist) > 0:
            return 'Pokemon already exist'
        else:
            actual = Pokemon.create(pk, name, height, weight)
            register_stats(actual, stats)
            insert_evolutions(data_chain['chain']['evolves_to'], [actual])
            return 'Pokemon has been registered'
    else:
        return 'Evolution chain with ID {0} does not exist'.format(evolution_chain_id)
