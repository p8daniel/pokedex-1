from pokedex.models.pokemon import Generation, Ability

def search_generations(query=None):

    if query is not None:
        generations=Generation.select().where(Generation.name == query)
    else:
        generations = Generation.select()

    return generations


def get_number_of_ability(generation):
    select=Ability.select().where(Ability.generation == generation)
    number=select.count()
    # print(number)
    return number