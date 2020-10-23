#sommets = ['s','a','b','c','d','e','f','g','t']
#Arcs = [('s','a',5),('s','b',10),('s','c',8),
#        ('a','c',10),('a','d',7),
#        ('b','d',8),('b','c',1),
#        ('c','e',2),('c','g',4),
#        ('d','f',7),
#        ('e','f',4),('e','g',2),('e','t',6),
#        ('f','t',10),
#        ('g','t',6)]
sommets = ['s','a','b','c','d','e','f','g','t']
Arcs = [('s','a',5),('s','b',6),('s','d',2),
        ('a','c',9),('a','f',12),('a','d',4),
        ('b','d',5),('b','g',13),('b','e',4),
        ('c','f',7),
        ('d','f',8),('d','t',20),('d','g',10),
        ('e','g',6),
        ('f','t',10)
        ]



def auplutot(Sommet):
    tots={}
    tots[Sommet]=-100
    for currentArc in Arcs :
        currentSommet = currentArc[0]
        if Sommet == currentSommet: # on vient de trouver un arc qui contient le sommet donner en paramètre     
            nextSommet = currentArc[1] 
            worktime = currentArc[2]
            if nextSommet == 'b':
                return worktime # worktime   
            x=auplutot(nextSommet)+worktime
            tots[Sommet]=max(x,tots[Sommet])
    return tots[Sommet]
            
print(auplutot('a'))