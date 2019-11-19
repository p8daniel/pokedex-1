from flask import Blueprint, request
from flask_restful import Api

from pokedex.errors import NotFoundError
from pokedex.models.database import db
from pokedex.managers.analytics import add_request_history

from .pokemons import Pokemon, Pokemons, Stats
from .species import Species, Specie
from .types import Types
from .abilities import Abilities
from .collections import User, Collections, Collection
from .consommables import Potion, PotionCollection
from .matches import Play
# from .species import Species, Specie, EggGroups
from .egg_groups import EggGroups
from .useragents import UserAgent
from .generations import Generation
from .scrapping import Scrapper

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


def register_api(app):
    # @app.route("/")  define an endpoint

    def get_my_ip():
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        request_data = {'method': request.method, 'url': request.url, 'ip': ip, 'parameters': request.args,
                        'user_agent': request.user_agent}
        return request_data

    @api_bp.before_request
    def before_request():
        db.connect(reuse_if_open=True)

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()

    @api_bp.errorhandler(NotFoundError)
    def if_not_found(error):
        response = {"error": f"{error.resource} {error.resource_id} not found"}
        return response, 404

    api.add_resource(Pokemons, '/pokemons')
    api.add_resource(Pokemon, '/pokemon/<pokemon_name>')
    api.add_resource(Species, '/species')
    api.add_resource(Specie, '/specie/<specie_id>')
    api.add_resource(Types, '/types')
    api.add_resource(EggGroups, '/egg-groups')
    api.add_resource(UserAgent, '/history')
    api.add_resource(Stats, '/stats')
    api.add_resource(User, '/user/<user_name>')
    api.add_resource(Collections, '/collections')
    api.add_resource(Collection, '/collection/<collection_name>')
    api.add_resource(Play, '/play')
    api.add_resource(Potion, '/consommables/potion')
    api.add_resource(PotionCollection, '/consommables/potioncollection')
    api.add_resource(Abilities, '/abilities')
    api.add_resource(Generation, '/generations')
    api.add_resource(Scrapper, '/scrapping')

    app.register_blueprint(api_bp, url_prefix="/api/v1")
