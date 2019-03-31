
import random 
import time


def Rand(start, end, num):
    for i in range(5):
        print("No HeartBeat")
        time.sleep(1)
    for i in range(num):
        print(random.randint(start, end))
        time.sleep(1)
    for i in range(3):
        print("No HeartBeat")
        time.sleep(1)

 
num = 7
start = 55
end = 63
Rand(start, end, num) 


