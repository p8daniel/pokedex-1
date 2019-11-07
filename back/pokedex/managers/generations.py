from pokedex.models.pokemon import Generation

def search_generations(query=None):

    if query is not None:
        generations=Generation.select().where(Generation.name == query)
    else:
        generations = Generation.select()

    return generations