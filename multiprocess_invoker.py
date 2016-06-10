import multiprocessing as mp
import time


#random piped fktn to simulate actual process
def piped_sleep(conn):
    conn.send("goodnight")       #send one msg initially, main prgrm waits until this msg

    #run infinite loop but keep pipe open to to be able o terminate it or whatever. Process can be daemn though
    while True:
        #simulate processing time
        time.sleep(5)
        #exception catching prob not necessary. Not sure how conn.recv() reallly behaves atm
        try:
			#try reading msgs from pipe. only one msg will be read at a time. Msgs are queued though.
            msg = conn.recv()
            #just example commands
            if msg == 'q':
                break
            elif msg == 'p':
                print "Test"
        except EOFError:
            pass

#launcher class for multiprocesses. Creates own process not just thread.
class MultiLauncher():
    def __init__(self, func):
        self.func = func
        #set up pipe to child process
        self.parent_conn, self.child_conn = mp.Pipe()
        self.p = mp.Process(name='daemon', target=func, args=(self.child_conn,))
        self.p.daemon = True

    def run(self):
        self.p.start()
        #Read inoming msg from pipe once. After that only unidirectional communication possible
        #In order to read from pipe, another thread has to be set here
        print(self.parent_conn.recv())

    #possibility to send msgs to child process
    def send(self, msg):
        self.parent_conn.send(msg)


if __name__ == '__main__':
    ml = MultiLauncher(piped_sleep)
    ml.run()
    ml.send('p')
    ml.send('q')
