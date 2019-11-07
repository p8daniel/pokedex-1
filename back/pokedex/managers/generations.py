from pokedex.models.pokemon import Generation

def search_generations():
    generations=Generation.select()

    return generations