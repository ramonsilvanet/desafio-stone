import threading, time, uuid

class Worker:

    id

    def __init__(self):
        self.id = uuid.uuid4()

    def execute(self, args):
        t1 = threading.Thread(target=self.__calculate(), args=(self, args))
        t1.start()
        t1.join()

    def __calculate(self, n):
        if n < 2:
            return n
        time.sleep(1) # wait 1 second
        return fibo_worker(self, n-1) + fibo_worker(self, n-2) 
