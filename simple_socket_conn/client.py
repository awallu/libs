import socket


def Main():
    """Client to server.py script. Establishes connection and allows for user input to be send to server."""
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    print(s.recv(1024))

    while True:
        message = raw_input("-> ")
        if message != '':
            s.send(message)
            data = s.recv(1024)
            print('Received from server: ' + data)
            if message == 'close_conn':
                break
    s.close()

if __name__ == '__main__':
    Main()
