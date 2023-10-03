from modules.pokemon import Pokemon

# Define the main menu function


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
            pokedex_number = int(
                input("Enter the Pokedex number of the Pokemon: "))
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
