import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"

pokemon_name = input('Enter the name of pokemon you want info for:')


url = f'{base_url}/{pokemon_name}'       # works with id or name
response = requests.get(url)

if response.status_code == 200:
    # print (response.json())
    data = response.json()            
else:
    raise Exception("Enter correct name!")