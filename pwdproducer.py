import threading
import queue

from password import Password
from pip._vendor.distlib.compat import raw_input


class PwdProducer(threading.Thread):

    def __init__(self,queue,condition):
        threading.Thread.__init__(self)
        self.condition = condition
        self.queue = queue


    def run(self):
        while(True):

            password = raw_input("Next password: ")
            self.condition.acquire()
            try:
                self.queue.put(Password(password), block=False)
                self.condition.notify()
            except queue.Full:
                self.condition.wait()
            self.condition.release()
