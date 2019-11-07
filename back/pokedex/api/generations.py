from flask import request
from flask_restful import Resource

from pokedex.managers.generations import search_generations, get_number_of_ability, get_number_of_type, create_new_generation


class Generation(Resource):
    def get(self):
        query = request.args.get('query', None)
        ask_ability_number = request.args.get('ability_number', 'false') == 'true'
        ask_type_number = request.args.get('type_number', 'false') == 'true'
        list_of_generation = search_generations(query)
        generations = []
        for generation in list_of_generation:
            mydict = generation.get_small_data()

            if ask_ability_number is True:
                ability_number = get_number_of_ability(generation)
                mydict['number_of_abilities'] = ability_number
            if ask_type_number is True:
                type_number = get_number_of_type(generation)
                mydict['number_of_types'] = type_number

            generations.append(mydict)

        return generations

    def put(self):
        generation_name = request.args['generation']
        create_new_generation(generation_name)


