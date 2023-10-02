# CS162-Pokemon-Battle-Simulator

This project will be a very basic text-based Pokemon battle simulator against a CPU that uses the Pokeapi to retrieve data. All moves will be randomized, and there will be an option to start your battle with randomized pokemon too.

Class: Pokemon

Methods:
get_data(Pokedex Number): perform api call and retrieve data. Will store in a class variable
get_base_stats(Pokemon): gets stats and applies natures effect to it
get_moves(Pokemon): gets moves
use_move(Pokemon, move): uses a move on opposing pokemon
get_nature(Pokemon)
get_type(Pokemon)
get_ivs(Pokemon): randomized ivs
get_evs(Pokemon): randomized evs
get_total_stats: calculates total stats based on level, iv, ev, and nature

Components:
Pokedex Number (int)
Type (str obj)
Level (int)
Stats (obj)
Nature (str)
Evolution Status (int)

Class: Battle

Methods:
get_user(Player): Gets user player object
get_cpu(Player): Gets cpu player object
display_battle_menu
get_faster_pokemon: checks the speed stat of both active pokemon, then returns the faster pokemon. This will determine who hits first
run_turn: Will run the turn with both player and CPU actions.
get_player_action
get_cpu_action: will randomize the CPU’s action

Components:
Player (obj)
CPU (obj)
Current turn (int): How many turns have passed

Class: Player

Methods:
append_pokemon(Pokedex Number?): Optional parameter to add a pokemon to the Player's team. If left blank, a random number will be generated.
get_team: gets player’s team. Will call append_pokemon
switch_pokemon(Pokemon): switches active player’s pokemon
attack:

Components:
active_pokemon (Pokemon): which pokemon is out in battle
Team (obj): array of pokemon objects. This will store all of their data, even if user switches out
