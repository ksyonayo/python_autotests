import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8d1c2aaa415931c5b647db53193aeef9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
trainer_id = '5540'

body_create = {
    "name": "Бульбазаврус",
    "photo_id": 123
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()["id"]

body_change_name = {
    "pokemon_id": pokemon_id,
    "name": "Котик",
    "photo_id": 123
}

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)