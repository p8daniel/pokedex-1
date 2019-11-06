from pokedex.models.collection import *


def add_pokemon_to_match(pokemon, player, match):
    new_pokemon_match = PokemonMatch.create(

        pokemon_id=pokemon.pokemon_id,
        name=pokemon.name,
        hp=pokemon.hp,
        special_attack=pokemon.special_attack,
        defense=pokemon.defense,
        attack=pokemon.attack,
        special_defense=pokemon.special_defense,
        speed=pokemon.speed,
        match=match,
        player=player
    )


def attack(pokemon_attack, pokemon_defend, attack_name='false'):
    """
    Fonction qui attaque un pokemon
    :param pokemon: autre pokemon a attaquer
    :return: point de vie de l'autre pokemon
    """
    # print(pokemon_attack.hp, pokemon_defend.hp, "inside function")

    attack_value = pokemon_attack.attack

    if attack_name is True:
        print('Waaa attack special!')
        attack_value = pokemon_attack.special_attack

    hp = pokemon_defend.take_damages(attack_value)
    return hp



def fight(pl1, pl2):
    match_histoty = []
    new_match = Match.create(player1=pl1, player2=pl2)
    collections_pl1 = Collection.select().where(Collection.user == pl1)
    collections_pl2 = Collection.select().where(Collection.user == pl2)

    if len(collections_pl1) == 0 or len(collections_pl2) == 0:
        match_histoty.append("One of the user has no collection")
        # print("not matching")
        return match_histoty

    collections_pl1 = collections_pl1[0]
    collections_pl2 = collections_pl2[0]

    pokemon_pl1 = PokemonCollection.select().where(PokemonCollection.collection == collections_pl1).limit(6)
    pokemon_pl2 = PokemonCollection.select().where(PokemonCollection.collection == collections_pl2).limit(6)

    for pokemon in pokemon_pl1:
        add_pokemon_to_match(pokemon, pl1, new_match)

    for pokemon in pokemon_pl2:
        add_pokemon_to_match(pokemon, pl2, new_match)

    # print("players are fighting")
    match_histoty.append("players are fighting")

    pokemon_alive_pl1 = PokemonMatch.select().where(PokemonMatch.match == new_match, PokemonMatch.player == pl1,
                                                    PokemonMatch.hp != 0)
    pokemon_alive_pl2 = PokemonMatch.select().where(PokemonMatch.match == new_match, PokemonMatch.player == pl2,
                                                    PokemonMatch.hp != 0)
    is_x = True
    while len(pokemon_alive_pl1) > 0 and len(pokemon_alive_pl2) > 0:

        # print("lenght", len(pokemon_alive_pl1), len(pokemon_alive_pl2))
        pokemon_pl1 = pokemon_alive_pl1[0]
        pokemon_pl2 = pokemon_alive_pl2[0]

        while pokemon_pl1.hp > 0 and pokemon_pl2.hp > 0:
            if is_x:
                match_histoty.append(pl1.name + " with " + pokemon_pl1.name + " attack " + pokemon_pl2.name)
                # print(pl1.name, " with ", pokemon_pl1.name, " attack ", pokemon_pl2.name)
                check_hp = attack(pokemon_pl1, pokemon_pl2)
                if check_hp == 0:
                    match_histoty.append(pokemon_pl2.name + " died")

            else:
                match_histoty.append(pl2.name + " with " + pokemon_pl2.name + " attack " + pokemon_pl1.name)
                # print(pl2.name, " with ", pokemon_pl2.name, " attack ", pokemon_pl1.name)
                check_hp = attack(pokemon_pl2, pokemon_pl1)
                if check_hp == 0:
                    match_histoty.append(pokemon_pl1.name + " died")

            is_x = not is_x

        pokemon_alive_pl1 = PokemonMatch.select().where(PokemonMatch.match == new_match, PokemonMatch.player == pl1,
                                                        PokemonMatch.hp != 0)
        pokemon_alive_pl2 = PokemonMatch.select().where(PokemonMatch.match == new_match, PokemonMatch.player == pl2,
                                                        PokemonMatch.hp != 0)

        if len(pokemon_alive_pl1) == 0:
            # print(pl1.name, "win")
            match_histoty.append(pl1.name + " win")
            break
        if len(pokemon_alive_pl2) == 0:
            # print(pl2.name, "win")
            match_histoty.append(pl2.name + " win")
            break


    return match_histoty
