sommets = ['s','a','b','c','d','e','f','g','t']
Arcs = [('s','a',5),('s','b',10),('s','c',8),
        ('a','c',10),('a','d',7),
        ('b','d',8),('b','c',1),
        ('c','e',2),('c','g',4),
        ('d','f',7),
        ('e','f',4),('e','g',2),('e','t',6),
        ('f','t',10),
        ('g','t',6)]

def auplutot(Sommet):
    tots={}
    tots[Sommet]=0
    for currentArc in Arcs :
        currentSommet = currentArc[0]
        if Sommet == currentSommet: # on vient de trouver un arc qui contient le sommet donner en paramètre     
            nextSommet = currentArc[1] 
            worktime = currentArc[2]
            if nextSommet == 't':
                return worktime # worktime   
            x=auplutot(nextSommet)+worktime
            tots[Sommet]=max(x,tots[Sommet])
    return tots[Sommet]
            

            
                

auplutot('s')
print(auplutot('s'))