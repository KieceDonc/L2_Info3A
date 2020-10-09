import random

def cons(t,q):
    return (t,q)

def hd(l):
    assert(None!=l)
    (t,q)=l
    return t

def tl(l):
    assert(None!=l)
    (t,q)=l
    return q

def iaj(i,j):
    if i==j:
        return cons(i,None)
    else:
        return cons(i,iaj(i+1,j))    

def lgr(l):
    if(None==l):
        return 0
    else:
        return 1+lgr(tl(l))


def map(f,l):
    if(None==l):
        return None
    else:
        return cons(f(hd(l)),map(f,tl(l)))
#t=iaj(1,10)
#print(hd(t))
#print(tl(t))
#print(map((lambda x:10*x),iaj(1,4)))

def foldl(op,ter,l): #Prend en parametre : 
    if None==l:
        return ter
    else:
        return foldl(op,op(ter,hd(l)),tl(l))

#print(foldl((lambda x,y: x+y),0,iaj(1,4)))

def filter(f,l):#Retourne une liste e 
                #Prend en parametre : Fonction qui retourne un boolean, liste
    if(None==l):
        return None
    elif(f(hd(l))):
        return cons(hd(l),filter(f,tl(l)))
    else :
        return filter(f,tl(l))


#print(filter((lambda x:0==x%2),iaj(1,6)))# rend la liste des entiers qui sont paires

def lalea(n,l):
    if(0==n):
        return l
    else:
        return lalea(n-1,cons(random.randint(1,1000),l))

def isempty(l):
    return None==l

def quickSort(cmpt,l):
    if None==l or None==tl(l):
        return l
    else :
        t=hd(l)
        petits= filter((lambda x: cmpt(x,t)<0),l)
        grands = filter((lambda x: cmpt(x,t)>0),l)
        egaux = filter((lambda x: cmpt(x,t)==0),l)
        return append(quickSort(cmpt,petits),append(egaux,quickSort(cmpt,grands)))

def append(a,b):
    if isempty(a):
        return b
    if isempty(b):
        return a
    return cons(hd(a),append(tl(a),b))

def checkSort(cmpt,l):
    if(None==l or None==tl(l)):
        return True
    else:
        return cmp(hd(l),hd(tl(l)))<=0 and checkSort(cmp,tl(l))
    


#l = lalea(20,None)
#print(l)
#l = quickSort((lambda a,b:a-b),l)
#print(l)
#print(checkSort((lambda a,b:a-b),l))

def moitie(l):
    if None==l or None==tl(l):
        return l
    else:
        return(cons(hd(l),moitie(tl(tl(l)))))

def fusion(cmp,a,b):
    if None == a :
        return b
    elif None==b:
        return a
    elif cmp(hd(a),hd(b))<0:
        return cons(hd(a),fusion(cmp,tl(a),b))
    else :
        return cons(hd(b),fusion(cmp,a,tl(b)))

def trifusion(cmp,l):
    if None==l or None==tl(l) :
        return l
    else : return fusion(cmp,trifusion(cmp,moitie(l)),trifusion(cmp,moitie(tl(l))))

l=lalea(20,None)
lt=trifusion((lambda a,b : a-b),l)
print(lt)
print(checkSort((lambda a,b : a-b),lt))