import threading
import queue

class PwdConsumer(threading.Thread):

    def __init__(self,queue,condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        while(True):
            password = None
            self.condition.acquire()
            try:
                password = self.queue.get(block = False)
                self.condition.notify()
            except queue.Empty:
                self.condition.wait()
            self.condition.release()

            if not password is None:
                print("Testing with '123' = " +str(password.check("123")))
                character='a'
                for ch in range('a','z'):

