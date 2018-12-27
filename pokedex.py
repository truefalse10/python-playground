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

    print('----\nid: ', pokemon.get('id'))
    print('Pokemon: ', pokemon['name'])
    print('Type: ', [get_type_emoji(t) for t in types])


while exit_program == False:
    search_pokemon()
    search_again = input('\nwould you like to search another pokemon? (y/n)\n')
    exit_program = search_again != 'y'
