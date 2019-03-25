import threading
import queue
from pwdproducer import PwdProducer
from pwdconsumer import PwdConsumer

queue = queue.Queue(maxsize=10)
condition = threading.Condition()

producer = PwdProducer(queue,condition)
consumer = PwdConsumer(queue, condition)

producer.start()
consumer.start()

producer.join()
consumer.join()
