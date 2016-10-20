from collections import namedtuple
import socket


CfourConnection = namedtuple('CfourConnection', ['socket', 'input', 'output'])

class CfourError(Exception):
    pass
                             

def connect (host: str, port: int) -> CfourConnection:
    cfour_socket = socket.socket()
    
    cfour_socket.connect((host, port))

    cfour_input = cfour_socket.makefile('r')
    cfour_output = cfour_socket.makefile('w')

    return CfourConnection(
        socket = cfour_socket,
        input = cfour_input,
        output = cfour_output)


def hello (connection: CfourConnection, username: str) -> None:
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    _expect_line(connection, 'WELCOME ' + username)
    _write_line(connection, 'AI_GAME')
    _expect_line(connection, 'READY')


                
def _read_line(connection: CfourConnection) -> str:
    '''Reads a line of text sent from the server and returns it without
    a newline at the end'''
    return connection.input.readline()[:-1]



def _expect_line(connection: CfourConnection, expected: str) -> None:
    '''Reads text sent from server, expecting it to contain a particular text.
    If the receieved line is different, it raises an exception; otherwise function has no effect'''

    line = _read_line(connection)

    if line != expected:
        raise CfourError()



def _write_line(connection: CfourConnection, line: str) -> None:
    '''Writes a line of text to the server, including the appropriate
    newline sequence & ensures that it's sent immediately.'''
    
    connection.output.write(line + '\r\n')
    connection.output.flush()




def close(connection: CfourConnection) -> None:
    'Closes the connection to the Connect Four server'
    connection.input.close()
    connection.output.close()
    connection.socket.close()


    
