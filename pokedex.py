import requests

BASE_URL = 'https://pokeapi.co/api/v2/'
exit_program = False


def search_pokemon():

    user_input = input('what pokemon would you like to search?\n')

    req = requests.get(BASE_URL + 'pokemon/' + user_input + '/')

    if not req.ok and req.status_code == 404:
        print('pokemon not found!')
        return

    pokemon = req.json()

    types = [t['type']['name'] for t in pokemon['types']]  # list comprehension

    def get_type_emoji(t):
        # python has no switch statement so we use dictionary
        switcher = {
            'grass': '🌱',
            'fire': '🔥',
            'water': '💧',
        }
        return switcher.get(t, '﹖(' + t + ')')

    def get_evolutions(pokemon_id):
        req = requests.get(BASE_URL + 'evolution-chain/' + str(pokemon_id))
        evolutions = [evolution['species']['name']
                      for evolution in req.json()['chain']['evolves_to']]
        return evolutions

    print('----\nid: ', pokemon.get('id'))
    print('Pokemon: ', pokemon['name'])
    print('Type: ', [get_type_emoji(t) for t in types])
    print('Evolutions:', get_evolutions(pokemon.get('id')))


while not exit_program:
    search_pokemon()
    search_again = input('\nwould you like to search another pokemon? (y/n)\n')
    exit_program = search_again != 'y'
