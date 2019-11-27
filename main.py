empty_box_char = '-'
gb=[[empty_box_char, empty_box_char, empty_box_char],[empty_box_char, empty_box_char, empty_box_char],[empty_box_char, empty_box_char, empty_box_char]]
is_game_won = False
is_game_ended = False
current_turn="X"

def start_game():
    show_game()
    play_turn()



def _is_int(val):
    try :
        int(val)
        return True
    except ValueError:
        return False

def show_game():
    print('\n============[ TIC TAC TOE ]=========\n')
    print('\t     0    1    2')
    for index,row in enumerate(gb): 
        print('\t',index,row)

def switch_turns():
    global current_turn
    if current_turn == 'X':
       current_turn='O'
    else:
       current_turn='X'

def play_turn():
    print('\n')
    msg = current_turn,"turn - what is your next Move (row,column) ? "
    location = input(msg)
    if _is_int(location[0]) and _is_int(location[2]):
        edit_board(int(location[0]),int(location[2]))
    else:
        print('invalid operation..')
        play_turn()

def edit_board(row,column):
    if gb[row][column]==empty_box_char:
        gb[row][column]= current_turn
        check_winners_if_any()
        switch_turns()
    else:
        print('invalid operation.. box already used')
        play_turn()

def check_winners_if_any():
    #check horizontally
    if is_the_same(gb[0][0],gb[0][1],gb[0][2]) or is_the_same(gb[1][0],gb[1][1],gb[1][2]) or is_the_same(gb[2][0],gb[2][1],gb[2][2]):
        game_won()
    #check vertically
    if is_the_same(gb[0][0],gb[1][0],gb[2][0]) or is_the_same(gb[0][1],gb[1][1],gb[2][1]) or is_the_same(gb[0][2],gb[1][2],gb[2][2]):
        game_won()
    #check diagonally
    if is_the_same(gb[0][0],gb[1][1],gb[2][2]) or is_the_same(gb[0][2],gb[1][1],gb[0][1]):
        game_won()
    
def game_won():
    global is_game_won
    if is_game_won== False:
        is_game_won=True
        print ('\ngame won !! the winner is',current_turn,' ')


def is_the_same(*args):
    first=args[0]
    if first!=empty_box_char:
        result= True
        for a in args:
            if a!= first:
                result = False
        return result
    else:
        return False

while is_game_won==False:
    start_game()