from database import Database
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
# db.resetDatabase()

_pokedex = Pokedex(db)

_pokedex.getPokemonByName("Bulbasaur")
_pokedex.getPokemonByType(["Grass", "Poison"])
_pokedex.getHeavyPokemon()
_pokedex.getLightPokemon()
_pokedex.getPokemonsWeakAgainst(["Fire"])

