def swap(t,a,b):
    n=0
    n=t[a]
    t[a]=t[b]
    t[b]=n

def partition(t, start, end):
    pIndex=end
    for i in range(start,end):
        if t[i]<=t[pIndex]:
            swap(t,i,pIndex)
            pIndex=i
        swap(t,pIndex,end)
    return pIndex

def quickSort(t,start,end):
    if(start>=end) : 
        return
    pInd = partition(t,start,end)
    quickSort(t,start,pInd)
    quickSort(t,pInd+1,end)


tab=[4,7,45,12,3,1]
partition(tab,0,5)
print(tab)