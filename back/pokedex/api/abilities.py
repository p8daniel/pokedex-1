from flask import request
from flask_restful import Resource

from pokedex.managers.abilities import get_abilities, get_pokemons_from_ability, add_ability


class Abilities(Resource):
    def get(self):
        pokemons = request.args.get('pokemons', 'false') == 'true'
        ask_effects = request.args.get('effects', 'false') == 'true'
        limit = request.args.get('limit', None)
        offset = request.args.get('offset', None)

        unused = request.args.get('unused', 'false') == 'true'
        query_gerneration = request.args.get('generation', None)
        search = request.args.get('query')
        abilities = get_abilities(search, unused, query_gerneration)

        result = []
        for ability in abilities:
            ability_result = ability.get_small_data(ask_effects)

            if pokemons:
                ability_result['pokemons'] = []
                pokemons_of_this_ability = get_pokemons_from_ability(ability.id)
                for pokemon in pokemons_of_this_ability:
                    pokemon_result = {'id': pokemon.id, 'name': pokemon.name}
                    ability_result['pokemons'].append(pokemon_result)

            result.append(ability_result)

        if offset is not None:
            result = result[int(offset):]
        if limit is not None:
            result = result[:int(limit)]

        return result

    def put(self):
        name = request.json['name']
        generation_name = request.json['generation']
        new_ability = add_ability(name, generation_name)
        return new_ability.get_small_data()
