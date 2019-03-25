import threading
import queue
from itertools import chain, product


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
                print(self.bruteforce(4))

    def bruteforce(charset, maxlength):
        return (''.join(candidate)
                for candidate in chain.from_iterable(product(charset, repeat=i)
                                                     for i in range(1, maxlength + 1)))
