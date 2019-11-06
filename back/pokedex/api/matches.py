from flask import request
from flask_restful import Resource

from pokedex.managers.collections import get_user_by_name
from pokedex.managers.matches import fight



class Play(Resource):
    def get(self):
        match_log = []

        player1_name = request.args['player1']
        player2_name = request.args['player2']
        player1 = get_user_by_name(player1_name)
        if player1 is None:
            return {'msg': 'Player1 not found'}, 404
        print(player1.name)
        match_log.append("Player1 is " + player1.name)

        player2 = get_user_by_name(player2_name)
        if player2 is None:
            return {'msg': 'Player2 not found'}, 404
        print(player2.name)
        match_log.append("Player2 is " + player2.name)

        text_result = fight(player1, player2)
        match_log.append(text_result)
        return match_log
