from pokedex.models.pokemon import Generation, Ability, Type


def search_generations(query=None):
    if query is not None:
        generations = Generation.select().where(Generation.name == query)
    else:
        generations = Generation.select()

    return generations


def get_number_of_ability(generation):
    select = Ability.select().where(Ability.generation == generation)
    number = select.count()
    # print(number)
    return number


def get_number_of_type(generation):
    select = Type.select().where(Type.generation == generation)
    number = select.count()
    return number


def create_new_generation(generation_name):
    Generation.create(name=generation_name)
