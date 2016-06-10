import threading, Queue
import time

#create extra thread to enable communication to user from console
class user_input_thread(threading.Thread):
    def __init__(self, queue):
        self.q = queue
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
				#define valid user inputs here. Eg 'q' to quit
                if raw_input("Enter \'q\' to quit: ")[0] == "q":
                    self.q.put("q")
                    break
			#empty raw_input error
            except IndexError:
                pass


#Queue user inputs
user_input_queue = Queue.Queue()
user_input = user_input_thread(user_input_queue)
user_input.start()

#Main program loop. Without input thread, program would not be responsive
#Alternative to this script would be to run the program in extra thread, to ensure responsivity of normal python console during execution
i = 0
while True:
    if i >= 1:                      #Max number of cycles to run
        break
	#catch user inputs
    if not user_input_queue.empty():
        if user_input_queue.get() == "q":
            break
    i += 1