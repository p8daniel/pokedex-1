import requests

from pokedex.models.pokemon import Ability, Generation, AbilityEffects, VerboseEffect, Language, PokemonAbilities, \
    Pokemon


def load_ability_from_api(name):
    request = requests.get(f'https://pokeapi.co/api/v2/ability/{name}')
    data = request.json()

    generation = Generation.get_or_none(name=data['generation']['name'])
    if generation is None:
        generation = Generation.create(name=data['generation']['name'])

    ability = Ability.get_or_none(name=name)
    if ability is None:
        db_data = {'name': data['name'], 'is_main_series': data['is_main_series'], 'generation': generation}
        ability = Ability.create(**db_data)

    AbilityEffects.delete().where(AbilityEffects.ability == ability).execute()
    for effect in data['effect_entries']:
        verbose_effect = VerboseEffect.get_or_none(short_effect=effect['short_effect'])
        if verbose_effect is None:
            language = Language.get_or_none(name=effect['language']['name'])
            if language is None:
                language = Language.create(name=effect['language']['name'])
            verbose_effect = VerboseEffect.create(effect=effect['effect'], short_effect=effect['short_effect'],
                                                  language=language)
        ability_effect = AbilityEffects.create(ability=ability, effect=verbose_effect)

    return ability


def load_abilities_from_api():
    i = 0

    next_page = 'https://pokeapi.co/api/v2/ability/'
    while next_page is not None:
        request = requests.get(next_page)
        data = request.json()

        next_page = data['next']

        for ability in data['results']:
            load_ability_from_api(ability['name'])
            i += 1

        print(f'{i} abilities loaded.')

    return i


def get_abilities(search=None, unused=False, query_gerneration=None):
    abilities = []

    if search is None:
        search = ""

    abilities = []
    for ability in Ability.select().order_by(Ability.id):
        if search in ability.name:
            abilities.append(ability)

    if unused:
        abilities = [ability for ability in abilities if len(ability.pokemons) == 0]
    if query_gerneration is not None:

        filtered_abilities = []
        for ability in abilities:

            # abilities = []

            generation_de_ce_ability = Generation.select().where(Generation.id == ability.generation)
            # print((generation_de_ce_ability[0].name))
            if query_gerneration in generation_de_ce_ability[0].name:
                filtered_abilities.append(ability)
        abilities = filtered_abilities

    return abilities


def add_ability(name, generation_name):
    generation = Generation.get_or_none(Generation.name == generation_name)
    if generation is None:
        generation = Generation.create(name=generation_name)

    new_ability = Ability.create(name=name, generation=generation)
    return new_ability


def get_pokemons_from_ability(ability_id):
    pokemons = []
    pokemon_abilities = PokemonAbilities.select(PokemonAbilities, Pokemon).join(Pokemon).where(
        PokemonAbilities.ability == ability_id)
    for pokemon_ability in pokemon_abilities:
        pokemons.append(pokemon_ability.pokemon)
    return pokemons
