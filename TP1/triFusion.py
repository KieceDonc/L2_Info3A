import math
import random
def createTab(n):
    return[random.randint(1,n*5) for i in range(1,n+1)]

def fusion(t,L,R):
    nL = len(L)
    nR = len(R)
    i = 0
    j = 0
    k = 0 
    while i<nL and j<nR:
        if L[i]<R[j]:
            t[k]=L[i]
            i+=1
        else:
            t[k]=R[j]
            j+=1
        k+=1
    while i<nL:
        t[k]=L[i]
        i+=1
        k+=1
    while j<nR:
        t[k]=R[j]
        j+=1
        k+=1

def triFusion(t):
    n = len(t)
    if n==1:
        return t
    m=n/2
    L = [None]*m
    for x in range(m) : 
        L[x] = t[x]
    R = [None]*(n-m)
    for y in range(0,(n-m),1) :
        R[y] = t[y+m]
    triFusion(L)
    triFusion(R)
    fusion(t,L,R)
tab = createTab(20000)
print(tab)
triFusion(tab)
print(tab)