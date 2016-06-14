"""Queueing of tasks for single background thread.
Written for Python 3."""

import threading
import queue
import time, random


class Worker(threading.Thread):
    """Class for threaded workers that will execute whaever their task is. The current plan is to use this architecture
    for the attocube or suruga seiki controllers. Each movement will take some time, all inputs (by GUI) in the meantime
    will be queued and execued one after another.
    Flexible function launcher is available in \libs\threaded_function_invoker."""

    def __init__(self, q):
        self.__queue = q
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        #Overridden 'run' from the threading module. Curently refers to run_once or run_forever or whatever. Can also
        # copy this code here.
        self.run_forever()

    def run_once(self):
        #Single task to be execued
        item = self.__queue.get()
        if item is None:
            return
        # pretend we're doing something that takes 10-100 ms
        time.sleep(random.randint(1, 10))
        print("task " + str(item) + " finished")
        print("what should I do now? ")

    def run_forever(self):
        #Loop and take new input tasks from the queue. Intended to be strings containing commandos to be sent to
        #motion controllers via telnet
        while True:
            item = self.__queue.get()
            if item is None:
                break
            # pretend we're doing something that takes 10-100 ms
            time.sleep(random.randint(1, 10))
            print("task " + str(item) + " finished")
            print("what should I do now? ")


def main():
    q = queue.Queue(0)
    w = Worker(q)
    w.start()

    while True:
        inp = input("what should I do now?\n")
        if inp != '':
            if inp == 'q':
                break

            q.put(inp)

if __name__ == '__main__':
    main()
