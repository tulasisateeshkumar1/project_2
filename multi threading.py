from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(10):
             sleep(1)
             print("Hello World")

class hi(Thread):
    def run(self):
        for i in range(10):
            sleep(1)
            print("Hi World")
r1=hello()
r2=hi()

r1.start()
sleep(.2)
r2.start()

r1.join()
r2.join()

print("Bye")