from flask import request
from flask_restful import Resource
from pokedex.managers.scrapping import load_pokemons_from_wikipedia, get_wiki_pokemons_from_db


class Scrapper(Resource):
    def get(self):
        result=[]
        pokemons=get_wiki_pokemons_from_db()
        for pokemon in pokemons:
            result.append(pokemon.get_small_data())
        return result

    def post(self):
        load_pokemons_from_wikipedia()
        # check=self.get()
        # return check


