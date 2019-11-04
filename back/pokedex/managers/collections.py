# import requests
# from playhouse.shortcuts import update_model_from_dict
# from peewee import fn
from pokedex.models.collection import User, Collection, PokemonCollection


def create_new_user(name):
    User.create(name=name)


def create_a_new_collection(name, user):
    Collection.create(name=name, user=user)


def add_pokemon_to_collection(pokemon, collection):
    PokemonCollection.create(

        collection=collection,

        pokemon_id=pokemon.id,
        pokemon_name=pokemon.name,
        pokemon_hp=pokemon.hp,
        pokemon_special_attack=pokemon.special_attack,
        pokemon_defense=pokemon.defense,
        pokemon_attack=pokemon.attack,
        pokemon_special_defense=pokemon.special_defense,
        pokemon_speed=pokemon.speed,
    )

def delete_pokemon_from_collection(pokemon, collection):
    selected_pokemons = PokemonCollection.select().where(PokemonCollection.pokemon_name == pokemon.pokemon_name,
                                                         PokemonCollection.collection == collection)
    selected_pokemons.delete()


# def update_pokemon(pokemon, stat_name, stat_value):
#     pokemon.stat_name=stat_value
#     pokemon.save()


def get_pokemon_list(collection):
    selected_pokemons = PokemonCollection.select().where(PokemonCollection.collection == collection)
    return selected_pokemons

