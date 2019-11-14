import requests
from lxml import html

from tqdm import tqdm

from pokedex.models.scrapping import Pokemon


def load_pokemons_from_wikipedia():
    wikipedia_request = requests.get('https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon')
    xpath = '/ html / body / div[3] / div[3] / div[4] / div / table[3]'

    tree = html.fromstring(wikipedia_request.content)
    pokemons_tables = tree.xpath(xpath)

    pokemons_table = pokemons_tables[0]
    pokemons_table_rows = pokemons_table.findall('.//tr')

    pokemons = {}
    generations=['generation-i','generation-ii','generation-iii','generation-iv','generation-v','generation-vi','generation-vii','generation-viii']

    for row in pokemons_table_rows[2:]:
        pokemon_id = None

        i = 0
        gen_cont = 0
        for column in row.findall('td'):
            # print(gen_cont)
            if i % 2 == 0:
                content = column.text_content()
                if 'No additional' not in content:
                    pokemon_id = int(content)
                    pokemons[pokemon_id] = None
                else:
                    i += 1
                    gen_cont += 1
            else:
                symbols_to_strip = ['\n', '※', '♭','♯','~','♭[e]', ]
                pokemon_name = column.text_content()


                for symbol in symbols_to_strip:
                    pokemon_name = pokemon_name.strip(symbol)
                    pokemon_gen=generations[gen_cont]
                # print(pokemon_name)
                pokemon_name = pokemon_name.rstrip()
                if pokemon_id is not None:
                    pokemons[pokemon_id] = []
                    pokemons[pokemon_id].append(pokemon_name)
                    pokemons[pokemon_id].append(pokemon_gen)
                    pokemon_id = None
                    gen_cont += 1

            i += 1


    Pokemon.delete().execute()
    for pokemon_id in tqdm(pokemons.keys()):
        pokemon_name, pokemon_gen = pokemons[pokemon_id]

        Pokemon.create(id=pokemon_id, name=pokemon_name, generation=pokemon_gen)




def get_wiki_pokemons_from_db():
    pokemons=Pokemon.select().order_by(Pokemon.id)
    return pokemons