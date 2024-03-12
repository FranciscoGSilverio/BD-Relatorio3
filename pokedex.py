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

    def getPokemonsWithMultiplier(self):
        heavy_pokemons = self.db.collection.find(
            {"multipliers": {"$exists": True}})
        write_a_json(heavy_pokemons, "pokemons_with_multiplier")

    def getPokemonWith2Weaknessess(self):
        light_pokemons = self.db.collection.find({"weaknesses": {"$size": 2}})
        write_a_json(light_pokemons, "pokemons_with_2_weaknessess")

    def getPokemonsWeakAgainst(self, type: list):
        pokemons_weak_against = self.db.collection.find(
            {"weaknesses": {"$in": type}})
        write_a_json(pokemons_weak_against, "pokemons_weak_against")
