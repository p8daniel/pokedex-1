from pokedex.models.consommable import Potion, PotionCollection
from pokedex.models.collection import PokemonCollection
from pokedex.managers.pokemons import get_pokemon_by_name


def apply_potion_to_pokemon_collection(pokemon_collection):
    get_potion=Potion.get_or_none(amount=10)
    if get_potion is None:
        print("No potion of amount 10")
    real_pokemon = get_pokemon_by_name(pokemon_collection.name)
    pokemon_collection.heal(get_potion.amount, real_pokemon.hp)



def apply_potion_to_collection(collection):
    get_potion=PotionCollection.get_or_none(amount=10)
    if get_potion is None:
        print("No potion for collections of amount 10")
    pokemon_collections=PokemonCollection.select().where(PokemonCollection.collection==collection)
    for pokemon in pokemon_collections:
        real_pokemon=get_pokemon_by_name(pokemon.name)
        pokemon.heal(get_potion.amount, real_pokemon.hp)


def create_new_potion(potion_amount):
    Potion.create(amount=potion_amount)

def create_new_potioncollection(potion_amount):
    PotionCollection.create(amount=potion_amount)