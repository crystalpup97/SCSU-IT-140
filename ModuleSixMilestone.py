#Chrissy Heisler
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
        }

current_room = 'Cellar'

while current_room != 'Exit':
    moves = rooms[current_room]
    print('You are in', current_room)
    print('You can move',moves)
    new_move=input('Enter your move:')
    if new_move in moves.keys():
        print('Valid move')
        current_room = moves[new_move]
    elif new_move == 'Exit' or new_move == 'exit':
        current_room = 'Exit'
    else:
        print('Invalid move')