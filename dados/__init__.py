import requests
import json

def personagem_ID(id):
    genshin = requests.get(f"https://gsi.fly.dev/characters/{id}")
    genshin = genshin.json()   
    genshin_name = genshin["result"]["name"]
    genshin_weapon = genshin["result"]["weapon"]
    genshin_vision = genshin["result"]["vision"]
    genshin_rarity = genshin["result"]["rarity"]
    genshin_title = genshin["result"]["title"]

    return f'Title: {genshin_title} , Nome: {genshin_name}, Arma: {genshin_weapon}, Visão: {genshin_vision} e Raridade: {genshin_rarity}'
def osPrimeirosNove():
    genshin = requests.get(f"https://gsi.fly.dev/characters")
    genshin = genshin.json() 

    for n in range(1,10):
        genshin_page = genshin["results"][n]["name"]
        genshin_page1 = genshin["results"][n]["weapon"]
        genshin_vision = genshin["results"][n]["vision"]
        genshin_rarity = genshin["results"][n]["rarity"]
        n =+ 1
        print(f'Nome: {genshin_page}, Arma: {genshin_page1}, Visao: {genshin_vision} e raridade: {genshin_rarity}')
        
def porNome(nome):
    genshin = requests.get(f"https://gsi.fly.dev/characters/search?name={nome}")
    genshin = genshin.json()
    genshin_name = genshin["results"][0]["name"]
    genshin_weapon = genshin["results"][0]["weapon"]
    genshin_vision = genshin["results"][0]["vision"]
    genshin_rarity = genshin["results"][0]["rarity"]

    return f'Nome: {genshin_name}, Arma: {genshin_weapon}, Visão: {genshin_vision} e Raridade: {genshin_rarity}'