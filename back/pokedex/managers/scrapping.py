import requests

def get_pokemons_from_wikipedia():
    wikipedia_request= requests.get()
    wikipedia_html=wikipedia_request.text
    print(wikipedia_html)