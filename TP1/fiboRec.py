def FiboRect(n):
    if n<2:return n
    return FiboRect(n-1)+FiboRect(n-2)

f0 = (FiboRect(4))
print(f0)
f1 = ([FiboRect(i) for i in range(4,24,3)])
print(f1)