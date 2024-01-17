from time import sleep
from threading import *

class Even(Thread):

    def run(self):
        for i in range(50):
            print("even=",(i+1)*2)
            sleep(2)

class Odd(Thread):

    def run(self):
        for i in range(50):
            print('odd=',i*2+1)
            sleep(2)


even = Even()
odd = Odd()

odd.start()
sleep(1)
even.start()