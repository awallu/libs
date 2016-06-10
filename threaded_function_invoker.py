import threading
import time


import sys

"""class to dynamically launch a function as separate thread. Thread runs to completion or main thread termination
no means of interacting with the thread are given here (eg terminate infinite loops by setting flags). Locks can be
applied in functions"""


class AsyncInvoker(threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.func = func
        self.daemon = True

    def run(self):
        self.func()


#example thread
def sleep():
    print "goodnight"
    time.sleep(5)
    print "goodmorning"


def start_thread(function):
    background = AsyncInvoker(function)
    background.start()
    print "The program can continue to run"

    #method to join several threads, ie wait for their completion
    #sbackground.join()
    #print "waited until thread is complete"


if __name__ == '__main__':
    #example process to be called
    #compare eg to '>>>sleep()'
    start_thread(sleep)
