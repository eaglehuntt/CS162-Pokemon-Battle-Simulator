from modules.pokemon import Pokemon

"""
Required modules: requests

pip install requests

----------------------


Tests:

Manually test that the stats are being calculated correctly:
https://pycosites.com/pkmn/stat.php

Manually test that if a user tries to view pokemon before they have created one

Manually test that if a user inputs a string program will catch it

Manually test that a user cannot input a number larger than 800

"""


def main_menu():
    print("Welcome to the Pokemon Management System!")
    pokemon = None  # Initialize pokemon object as None

    while True:
        print("\nMain Menu:")
        print("1. Create a new Pokemon")
        print("2. Display Pokemon Info")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                try:
                    pokedex_number = int(
                        input("Enter the Pokedex number of the Pokemon (1-800): "))
                    if 1 <= pokedex_number <= 800:
                        break  # Valid input, exit the loop
                    else:
                        print(
                            "Invalid Pokedex number. Please enter a number between 1 and 800.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            level = int(input("Enter the level of the Pokemon: "))

            # Create a new Pokemon object
            pokemon = Pokemon(pokedex_number=pokedex_number, level=level)
            print(f"New Pokemon '{pokemon.name}' created!")

        elif choice == "2":
            if pokemon:
                print("\nPokemon Info:")
                print(pokemon)
            else:
                print("No Pokemon created yet. Please create a Pokemon first.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()
