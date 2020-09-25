def triSelection(t):
    n = len(t) # length of t list
    for x in range(0,n-1):
        xmin = x
        for y in range(x+1,n):
            if(t[y]<t[xmin]):
                xmin = y
                tmp = t[x]
                t[x] = t[xmin]
                t[y]= tmp
    return t

randomList = [165574,3,5454,4,45,-1,1,3]
print(triSelection(randomList))