import requests as rq
import random
import math

# test: https://pycosites.com/pkmn/stat.php


class IncorrectNatureError(Exception):
    pass


class Pokemon:

    def __init__(self, pokedex_number, nature="random"):
        self.data = self._get_data(pokedex_number)
        self.level = 50
        self.type = self._get_type()

        # (name, (increased stat, decreased stat))
        self.nature_name, self.nature_effects = self._get_nature(nature)

        self.base_stats = self._get_base_stats()
        self.ivs = self._get_ivs()
        self.evs = self._get_evs()
        self.total_stats = self._get_total_stats()

    def _get_data(self, pokedex_number):
        pokemon_data = rq.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokedex_number}").json()

        return pokemon_data

    def _get_type(self):
        # Logic to check if pokemon is single or dual type
        if len(self.data["types"]) > 1:
            type1 = self.data["types"][0]["type"]["name"]
            type2 = self.data["types"][1]["type"]["name"]
            pokemon_type = [type1, type2]
        else:
            pokemon_type = [self.data["types"][0]["type"]["name"]]

        return pokemon_type

    def _get_nature(self, nature):

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

        if nature == "random":
            nature = random.choice(list(natures.keys()))

        elif nature != "random" and nature not in list(natures.keys()):
            raise IncorrectNatureError("The nature provided is not valid")

        stat_effect = natures[nature]

        return (nature, stat_effect)

    def _get_base_stats(self):
        # Logic to get base stat data and return it as a dictionary object
        stats_info = self.data["stats"]
        base_stats = {}

        for stat_object in stats_info:
            base_stats[stat_object["stat"]["name"]] = stat_object["base_stat"]

        return base_stats

    def _get_ivs(self):
        ivs = {}

        for stat in self.base_stats.keys():
            value = random.randint(0, 31)
            ivs[stat] = value

        return ivs

    def _get_evs(self):
        evs = {}

        # maximum total evs = 510
        maximum_evs_remaining = random.randint(0, 510)
        maximum_evs_per_stat = 252

        # Initialize all EVs to 0
        for stat in self.base_stats.keys():
            evs[stat] = 0

        while maximum_evs_remaining > 0:
            selected_stat = random.choice(list(evs.keys()))

            # Calculate the maximum EVs that can be added to this stat
            remaining_evs_for_stat = maximum_evs_per_stat - evs[selected_stat]

            if remaining_evs_for_stat > 0:
                # Distribute random EVs (up to the remaining limit) to the selected stat
                added_evs = random.randint(
                    0, min(remaining_evs_for_stat, maximum_evs_remaining))
                evs[selected_stat] += added_evs
                maximum_evs_remaining -= added_evs

        return evs

    def _get_total_stats(self):
        print(f"IVs: {self.ivs}")
        print(f"EVs: {self.evs}")
        print(f"Base Stats: {self.base_stats}")
        print(f"Nature: {self.nature_name}")

        # Calculation based on Generation III onward formula.
        # https://pokemon.fandom.com/wiki/Statistics#

        stats = {}

        for stat in self.base_stats.keys():
            base_stat = self.base_stats[stat]
            iv = self.ivs[stat]
            ev = self.evs[stat]
            level = self.level

            if stat == "hp":
                hp_stat = math.floor(((2 * base_stat + iv + (ev // 4))
                                      * level // 100) + level + 10)
                stats["hp"] = hp_stat
            else:
                other_stat = math.floor((((2 * base_stat + iv + (ev // 4)) *
                                          level // 100) + 5) * self.nature_multiplier(stat))
                stats[stat] = other_stat

        print(stats)

        return stats

    def nature_multiplier(self, stat):
        increased_stat, decreased_stat = self.nature_effects

        if stat == increased_stat:
            return 1.1
        elif stat == decreased_stat:
            return 0.9
        else:
            return 1.0


pkm = Pokemon(1)
