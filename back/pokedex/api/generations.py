from flask import request
from flask_restful import Resource

from pokedex.managers.generations import search_generations

class Generation(Resource):
    def get(self):
        query = request.args.get('query', None)
        list_of_generation=search_generations(query)
        generations=[generation.get_small_data() for generation in list_of_generation]
        return generations