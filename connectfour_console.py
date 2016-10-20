#29211757 Kevin Yin and 72238150 Jenny Kim, Project 2
#This module contains the interface for a local Connect 4 game played on the console.

from connectfour import *
from collections import namedtuple

ConnectFour_Turn= namedtuple('ConnectFour_Turn', 'gamestate turntype column')

def playgame():
    game_state= new_game_state()
    print("You have started a new game of connect four.")
   
    while True:
        column = None
        print('')
        print_board(game_state)

        #Determing whether a player has won
        outcome= winning_player(game_state)
        if outcome == RED:
            print("Congratulations! RED player has won.")
            break
        elif outcome == YELLOW:
            print("Congratulations! YELLOW player has won.")
            break
                
        #Basic move structure
        if game_state.turn == RED:
            print("It is RED turn.")
        elif game_state.turn == YELLOW:
            print("It is YELLOW turn.")
        turn_type= input('DROP or POP? ').upper()

        if turn_type != 'DROP' and turn_type != 'POP':
            print('Please enter a valid command, either DROP or POP.')

        else:
            try:
                column= int(input('Enter column number: ')) - 1
                game_state= make_move(game_state, turn_type, column)
            except:
                print('Please enter a valid column number.')


def print_board(state: ConnectFourGameState):
    '''Prints a visible representation of the game board given the state.
    '''
    string1 = '    '
    for column in range(BOARD_COLUMNS):
        column += 1
        string1= string1 + str(column) + '  '
    print(string1)
    for row in range(BOARD_ROWS):
        string2= '    '
        for column in range(BOARD_COLUMNS):
            if state.board[column][row] == NONE:
                string2 += '.'
            elif state.board[column][row] == RED:
                string2 += 'R'
            else:
                string2 += 'Y'
            string2 += '  '
        print(string2)

def make_move(game_state: 'game state', turn_type: str, column: int) -> ConnectFourGameState:
    '''Asks the user for a column number and turn type and returns a new ConnectFourGameState.
    '''

    if turn_type== 'DROP':
        try:
            game_state= drop_piece(game_state, column)
        except ValueError:
            print('Invalid column number, please try again.')
            
    elif turn_type== 'POP':
        try:
            game_state= pop_piece(game_state, int(column))
        except ValueError:
            print('Invalid column number, please try again.')
        except InvalidMoveError:
            print('You cannot pop from that column.')

    return game_state



if __name__ == '__main__':
    playgame()


                
            


               
            
            
    
        
    
