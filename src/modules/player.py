import pokemon
import random


class Player:

    def __init__(self, name="Red", team=[]):
        # array of pokemon objects
        self.team = self._get_team(team)

        # player starts off with first pokemon as active
        self.active_pokemon = self.team[0]

    def _get_team(self, team):
        if team == []:
            for i in range(6):
                selected_pokemon = self._choose_pokemon()
                team.append(pokemon.Pokemon(selected_pokemon))
        return team

    def _choose_pokemon(self, pokedex_number=0):
        available_pokemon = 807

        if pokedex_number == 0:
            return random.randint(1, 807)
        else:
            try:
                return pokedex_number
            except ValueError:
                print(
                    f"Failed to get pokedex_number: {pokedex_number} is not a valid integer.")

    def switch_active_pokemon(self, index):
        try:
            self.active_pokemon = self.team[index]
        except ValueError:
            print("Error: Enter [0-5]")
        except IndexError:
            print(f"Error: {index} is out of the range [0-5]")


red = Player()

print(red.team)
print(red.active_pokemon.name)
red.switch_active_pokemon(5)
print(red.active_pokemon.name)
red.switch_active_pokemon(6)
