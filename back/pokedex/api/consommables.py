from flask_restful import Resource
from flask import request

from pokedex.managers.collections import get_collection_by_name, get_pokemonscollection_by_name
from pokedex.managers.consommables import apply_potion_to_pokemon_collection, create_new_potion, \
    create_new_potioncollection, apply_potion_to_collection


class Potion(Resource):
    def put(self):
        potion_amount = request.args['amount']
        create_new_potion(potion_amount)

    def patch(self):
        collection_name = request.args['collection']
        collection = get_collection_by_name(collection_name)
        # if collection is None:
        #     return {'msg': 'Collection not found'}, 404

        pokemon_name = request.args['pokemon']
        # all_collection = request.args.get('all_collection', 'false') == 'true'
        pokemon_collection = get_pokemonscollection_by_name(pokemon_name, collection)
        # if pokemon_collection is None:
        #     return {'msg': 'Pokemon not found on this collection'}, 404
        apply_potion_to_pokemon_collection(pokemon_collection[0])


class PotionCollection(Resource):
    def patch(self):
        collection_name = request.args['collection']
        collection = get_collection_by_name(collection_name)
        # if collection is None:
        #     return {'msg': 'Collection not found'}, 404
        apply_potion_to_collection(collection)

    def put(self):
        potion_amount = request.args['amount']
        create_new_potioncollection(potion_amount)
