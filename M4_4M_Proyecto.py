import requests
import json
import os

def buscar_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        imagen = data['sprites']['front_default']
        peso = data['weight']
        altura = data['height']
        movimientos = [move['move']['name'] for move in data['moves']]
        habilidades = [ability['ability']['name'] for ability in data['abilities']]
        tipos = [type['type']['name'] for type in data['types']]
        return {
            "nombre": nombre_pokemon,
            "imagen": imagen,
            "peso": peso,
            "altura": altura,
            "movimientos": movimientos,
            "habilidades": habilidades,
            "tipos": tipos
        }
    else:
        return None

def guardar_pokemon_en_json(pokemon):
    if not os.path.exists('pokedex'):
        os.makedirs('pokedex')
    with open(f'pokedex/{pokemon["nombre"]}.json', 'w') as f:
        json.dump(pokemon, f, indent=4)

def main():
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
    pokemon = buscar_pokemon(nombre_pokemon)
    if pokemon:
        print("Imagen:", pokemon["imagen"])
        print("Peso:", pokemon["peso"])
        print("Altura:", pokemon["altura"])
        print("Movimientos:", pokemon["movimientos"])
        print("Habilidades:", pokemon["habilidades"])
        print("Tipos:", pokemon["tipos"])
        guardar_pokemon_en_json(pokemon)
    else:
        print("¡Pokémon no encontrado!")

if __name__ == "__main__":
    main()
