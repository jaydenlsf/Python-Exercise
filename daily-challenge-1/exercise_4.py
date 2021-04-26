player_1 = (input('Player 1: ')).lower()
player_2 = (input('Player 2: ')).lower()

win = {'r': 's', 'p': 'r', 's': 'p'}

if player_1 not in win or player_2 not in win:
    print('Invalid option.')
elif player_1 == win[player_2]:
    print('Player 2 wins!')
elif player_2 == win[player_1]:
    print('Player 1 wins!')
else:
    print('Tie!')