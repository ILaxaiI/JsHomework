import time
import explorerhat

global count = 14
def increment(n=1):
    count+=n


def decrement(n=-1):
    count+=n

def decToBin(n):
    if type(n) == int:
        binnum = [0]*4
        if n > 15:
            n%=16
            print("4 bit Integer overflow, truncating number")
        for i in range(3,-1,-1):
            binnum[i] = n%2 
            n//=2
        return binnum

def visualiseBin(m):
    binarr = decToBin(m)
    for i in range(0,4):
        if binarr[i] == 1:
            explorerhat.light[i].on()
        else:
            explorerhat.light[i].off()
        
#todo: make increment an event on press
visualiseBin(count)

time.sleep(100)
