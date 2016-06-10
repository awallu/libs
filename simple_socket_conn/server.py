import socket
from thread import start_new_thread


def server():
    """Server function: Establishes server functionality and listens to connection.
    Each new connection spawns a new thread. Functionality of the connection to be defined in threaded_client."""

    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print('waiting for connection..')

    #listen for connections
    while True:
        #accept everything
        conn, addr = s.accept()
        print('connected to: ' + addr[0] + ':' + str(addr[1]))
        conn.send('Welcome, type your info')

        try:
            #launch new threaded connection
            start_new_thread(threaded_client, (conn,))
        except socket.error as e:
            print('connection closed')


def threaded_client(conn):
    """Client for server connections. Provided functionality to be edited here"""
    while True:
        #buffer recieved data
        data = conn.recv(1024)

        #empty data recieved
        if not data:
            conn.send('what?')
        print("from connected user: " + data)

        #define server response here
        if data == 'close_conn':
            conn.send('bye')
            break
        else:
            #example server response
            data = data.upper()
            print("sending: " + data)
            conn.send(data)

    conn.close()


def Main():
    server()


if __name__ == '__main__':
    Main()
