from modules.pokemon import Pokemon


class Tests:

    def __init__(self):
        self.positive_tests = [self.create_pokemon, self.assign_nature]
        self.negative_tests = [self.invalid_pokedex_number]

    def run_all(self):
        self.run_positive()
        self.run_negative()

    def run_positive(self):
        for test in self.positive_tests:
            test()

    def run_negative(self):
        for test in self.negative_tests:
            test()

    def create_pokemon(self, pokedex_number=25, nature="adamant", level=50):
        try:
            pokemon = Pokemon(pokedex_number, nature, level)
            print("Positive Test: Pokemon created successfully.")
        except Exception as e:
            print(f"Error creating Pokemon: {e}")

    def assign_nature(self, pokedex_number=143, nature="bold", level=60):
        try:
            pokemon = Pokemon(pokedex_number, nature, level)
            assert pokemon.nature_name == "bold"
            print("Positive Test: Valid nature assigned successfully.")
        except Exception as e:
            print(f"Error assigning nature: {e}")

    def invalid_pokedex_number(self, pokedex_number=10000, nature="random", level=20):
        try:
            pokemon = Pokemon(pokedex_number, nature, level)
            print("Negative Test: Invalid Pokedex number not handled properly.")
        except Exception as e:
            print("Negative Test: Invalid Pokedex number correctly raised an error.")


if __name__ == "__main__":
    tests = Tests()
    tests.run_all()
