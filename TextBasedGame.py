# Chrissy Heisler
def show_instructions():
    print('Retail Text Adventure Game')
    print("Get the customer's seven items for their order before going outside to meet them, or they will complain to corporate.")
    print('Move commands: North, South, East, West')
    print('Add to inventory: get <item name>')
    print('-----------------------')

def main():
    show_instructions()
    rooms = {
        'Toys': {'South': 'Clothing', 'East': 'Home Goods', 'item': 'dollhouse'},
        'Home Goods': {'West': 'Toys', 'South': 'Food', 'item': 'carpet'},
        'Outside': {'South': 'Beauty', 'item': 'customer'},
        'Clothing': {'North': 'Toys', 'East': 'Food', 'South': 'Art Supplies', 'item': 'socks'},
        'Food': {'North': 'Home Goods', 'East': 'Beauty', 'South': 'Electronics', 'West': 'Clothing', 'item': 'bananas'},
        'Beauty': {'North': 'Outside', 'West': 'Food', 'item': 'lotion'},
        'Art': {'North': 'Clothing', 'East': 'Electronics', 'item': 'paint'},
        'Electronics': {'North': 'Food', 'East': 'Break Room', 'West': 'Art', 'item': 'earbuds'},
        'Break Room': {'West': 'Electronics', 'item': 'None'}
    }
    current_room = 'Break Room'
    Inventory = []

    while current_room != 'Outside':
        moves = rooms[current_room]
        print('*You are in', current_room, '*')
        print('You can move:')
        if 'North' in moves:
            print('- North:', moves['North'])
        if 'South' in moves:
            print('- South:',moves['South'])
        if 'East' in moves:
            print('- East: ', moves['East'])
        if 'West' in moves:
            print('- West: ', moves['West'])
        if rooms[current_room]['item'] != 'None':
            print('You see', rooms[current_room]['item'])
        print("Inventory: ", ', '.join(Inventory))
        new_move = input('>>>Enter your move: ')
        new_move = new_move.capitalize()
        if new_move in moves.keys():
            print('Valid move')
            current_room = moves[new_move]
        elif 'Get' in new_move:
            new_move = new_move.split()
            new_move = new_move[1].lower()
            if new_move == rooms[current_room]['item']:
                rooms[current_room]['item'] = 'None'
                Inventory.append(new_move)
            else:
                print('Invalid item')
        else:
            print('Invalid move')
        print('---------')

    if current_room == 'Outside':
        if len(Inventory) == 7:
            print('Congratulations! You got all the items for the customer!')
        elif len(Inventory) < 7:
            print("Sorry, you didn't get all the items for the customer. You were fired.")
main()