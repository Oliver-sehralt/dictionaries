def player_intro(dictionary):
    for key, val in dictionary.items():
        print(f'my favorite player is {key} and he is a {val}')

favorite_players = {}

while True:
    player_name = input('enter a players name:')
    player_position = input('enter the players position:')
    favorite_players[player_name] = player_position

    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

player_intro(favorite_players)
