
def FiboLoop(n):
    fim0 = 0 
    fim1 = 1
    
    for i in range(1,n):
        fi = fim0+fim1
        fim0 = fim1
        fim1=fi
    return fi

f0 = (FiboLoop(4))
print(f0)
f1 = [FiboLoop(i) for i in range(4,24,3)]
print(f1)