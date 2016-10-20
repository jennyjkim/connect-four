import connectfour_socket
import connectfour_console
import connectfour

CFOUR_HOST = 'woodhouse.ics.uci.edu'
CFOUR_PORT = 4444

def user_interface() -> None:
    '''Runs the console-mode user interface from start to finish'''
    print('Welcome to the game of Connect Four. You will be going against the AI')

    
    username = input('Login: ')
    print('Connecting...')
    connection = connectfour_socket.connect(CFOUR_HOST, CFOUR_PORT)
    print('Connected!')

    try:
        connectfour_socket.hello(connection, username)
        game_state = connectfour.new_game_state()
    
        while True:
            connectfour_console.print_board(game_state)
            outcome = connectfour.winning_player(game_state)
            if outcome == 1:
                print('RED player has won!')
                break
            if outcome == 2:
                print('YELLOW player has won!')
                break

            if game_state.turn == 1:
                print('It is RED (client) turn.')
                game_state = client_move(game_state, connection)

            if game_state.turn == 2:
                print('It is YELLOW (network) turn.')
                game_state = 
            
       
                

    except:
        print('ERROR!!!!')

    finally:
        connectfour_socket.close(connection)
        print('Connection closed')




def client_move(game_state: connectfour_console.ConnectFour_Turn, connection: connectfour_socket.CfourConnection) -> connectfour_console.ConnectFour_Turn:
    while True:
        move = input('DROP or POP? ').upper()
        if move != 'DROP' and move != 'POP':
            print('ERROR, please enter again.')

        else:
            try:
                column = int(input('Enter column number: ')) - 1
                game_state = connectfour_console.make_move(game_state, move, column)
                break
            except:
                print('Please enter a valid column number.')

    return game_state


def network_move(game_state: connectfour_console.ConnectFour_Turn, connection: connectfour_socket.CfourConnection) -> connectfour_console.ConnectFour_Turn:
    if connectfour_socket._read_line(connection) == 'OKAY':
        print('ok')
        





user_interface()
