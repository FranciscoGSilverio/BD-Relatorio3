from database import Database
from write_a_json import write_a_json

class Pokedex:
    def __init__(self, database: Database):
        self.db = database

    def getPokemonByName(self, name: str):
        pokemon = self.db.collection.find({"name": name})
        write_a_json(pokemon, "pokemon")

    def getPokemonByType(self, types: list):
        pokemons = self.db.collection.find({"type": {"$in": types}})
        write_a_json(pokemons, "pokemons_by_type")
    
    def getHeavyPokemon(self):
        heavy_pokemons = self.db.collection.find({"weight": {"$gt": 100}})
        write_a_json(heavy_pokemons, "heavy_pokemons")

    def getLightPokemon(self):
        light_pokemons = self.db.collection.find({"weight": {"$lt": 10}})
        write_a_json(light_pokemons, "light_pokemons")

    def getPokemonsWeakAgainst(self, type: list):
        pokemons_weak_against = self.db.collection.find({"weaknesses": {"$in": type}})
        write_a_json(pokemons_weak_against, "pokemons_weak_against")