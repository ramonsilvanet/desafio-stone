import threading, time, uuid
from threading import Thread

class Worker(Thread):

    def __init__(self, args):
        Thread.__init__(self)
        
        self._args = args
        self.id = uuid.uuid4()


    def run(self):
        self.__calculate(self, self._args)
    
    def __calculate(n):
        if n < 2:
            return n
        
        return self.__calculate(self, n-1) + self.__calculate(self, n-2)


    
