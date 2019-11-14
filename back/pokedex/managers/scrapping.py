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
    generations = ['generation-i', 'generation-ii', 'generation-iii', 'generation-iv', 'generation-v', 'generation-vi',
                   'generation-vii', 'generation-viii']

    specie_symbols = {'': None, '※': 'Baby Pokémon', '♭': 'Mythical Pokémon', '♯': 'Ultra Beast', '~': 'Fossil Pokémon'}
    specie_colors = {'background-color: #9FCADF': 'Starter Pokémon', 'background-color: #E89483': 'Legendary Pokémon'}
    for row in pokemons_table_rows[2:]:

        pokemon_id = None

        i = 0
        gen_cont = 0
        for column in row.findall('td'):

            if i % 2 == 0:
                content = column.text_content()
                if 'No additional' not in content:
                    pokemon_id = int(content)
                    pokemons[pokemon_id] = None
                else:
                    i += 1
                    gen_cont += 1
            else:
                symbols_to_strip = ['※', '♭', '♯', '~']
                pokemon_name = column.text_content()
                pokemon_symbol = ''
                pokemon_name = pokemon_name.strip('\n')
                pokemon_name = pokemon_name.strip('[e]')
                for symbol in symbols_to_strip:
                    if symbol in pokemon_name:
                        print(pokemon_name)
                        print(symbol)
                        pokemon_name = pokemon_name.strip(symbol)
                        print(pokemon_name)
                        pokemon_symbol = symbol
                pokemon_gen = generations[gen_cont]

                pokemon_name = pokemon_name.rstrip()
                if pokemon_id is not None:
                    pokemons[pokemon_id] = []
                    pokemons[pokemon_id].append(pokemon_name)
                    pokemons[pokemon_id].append(pokemon_gen)
                    if 'style' in column.attrib:
                        if column.attrib['style'] in specie_colors:
                            pokemons[pokemon_id].append(specie_colors[column.attrib['style']])

                    if len(pokemons[pokemon_id]) < 3:
                        pokemons[pokemon_id].append(specie_symbols[pokemon_symbol])

                    pokemon_id = None
                    gen_cont += 1

            i += 1

    Pokemon.delete().execute()
    for pokemon_id in tqdm(pokemons.keys()):
        pokemon_name, pokemon_gen, pokemon_specie = pokemons[pokemon_id]

        Pokemon.create(id=pokemon_id, name=pokemon_name, generation=pokemon_gen, specie=pokemon_specie)


def get_wiki_pokemons_from_db():
    pokemons = Pokemon.select().order_by(Pokemon.id)
    return pokemons
