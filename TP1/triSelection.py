import math
import random
def createTab(n):
    return[random.randint(1,n*5) for i in range(1,n+1)]

def triSelection(t):
    n = len(t) # length of t list
    for x in range(0,n-1):
        xmin = x
        for y in range(x+1,n):
            if(t[y]<t[xmin]): xmin = y
        tmp = t[xmin]
        t[xmin] = t[x]
        t[x]= tmp
    return t

randomList = createTab(10)
print(randomList)
print(triSelection(randomList))