import requests as rq
import random


class Pokemon:

    def __init__(self, pokedex_number):
        self.data = self.get_data(pokedex_number)
        self.type = self.get_type()
        self.nature = self.get_nature()  # (name, (increased stat, decreased stat))
        self.stats = self.get_stats()

    def get_data(self, pokedex_number):
        pokemon_data = rq.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokedex_number}").json()

        return pokemon_data

    def get_type(self):
        # Logic to check if pokemon is single or dual type
        if len(self.data["types"]) > 1:
            type1 = self.data["types"][0]["type"]["name"]
            type2 = self.data["types"][1]["type"]["name"]
            pokemon_type = [type1, type2]
        else:
            pokemon_type = [self.data["types"][0]["type"]["name"]]

        return pokemon_type

    def get_nature(self):

        # data from https://www.reddit.com/r/PokemonFireRed/comments/kqj010/nature_chart/

        # object structure:
        # nature : (increased stat, decreased stat)

        natures = {
            "lonely": ("attack", "defense"),
            "brave": ("attack", "speed"),
            "adamant": ("attack", "special-attack"),
            "naughty": ("attack", "special-defense"),
            "bold": ("defense", "attack"),
            "relaxed": ("defense", "speed"),
            "impish": ("defense", "special-attack"),
            "lax": ("defense",  "special-defense"),
            "timid": ("speed", "attack"),
            "hasty": ("speed", "defense"),
            "jolly": ("speed", "special-attack"),
            "naive": ("speed", "special-defense"),
            "modest": ("special-attack", "attack"),
            "mild": ("special-attack", "defense"),
            "quiet": ("special-attack", "speed"),
            "rash": ("special-attack", "special-defense"),
            "calm": ("special-defense", "attack"),
            "gentle": ("special-defense", "defense"),
            "sassy": ("special-defense", "speed"),
            "careful": ("special-defense", "special-attack"),
        }

        selected_nature = random.choice(list(natures.keys()))
        stat_effect = natures[selected_nature]

        return (selected_nature, stat_effect)

    def get_stats(self):
        # Logic to get base stat data and return it as a dictionary object
        stats_info = self.data["stats"]
        base_stats = {}

        for stat_object in stats_info:
            base_stats[stat_object["stat"]["name"]] = stat_object["base_stat"]

        # apply nature to stats
        nature_effect = self.nature[1]

        return base_stats


pkm = Pokemon(1)

print(pkm.stats)
