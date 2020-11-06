"""
arcs=[ (0, 1, 100), (0, 2, 200), (1, 3, 50), (1, 4, 60), (2, 3, 70),
(2, 4, 80), (3, 5, 10), (4, 5, 20) ]
sommets=[0, 1, 2, 3, 4, 5]
source=0
terminal=5
"""
arcs=[
(0, 1, 4), (0, 2, 6),(0, 4, 2),  
(1, 3, 6), (1, 4, 4), (1, 5, 12),
(2, 4, 5), (2, 6, 13), 
(3, 5, 7), 
(4, 5, 8), (4, 7, 20), (4, 6, 10),
(5, 7, 0), 
(6, 7, 5) ]
sommets=[0, 1, 2, 3, 4, 5, 6, 7]
source=0
terminal=7
tots={}
tots[ source ]=0
def auplustot( s ) :
  if tots.has_key(s) :
    return tots[s]
  else :
    x = -100
    for (a, b, ab) in arcs :
      assert( a != terminal)
      assert( b != source)
      if b==s :
        x = max( x, auplustot(a) + ab)
        tots[s]= x
    return tots[s]
auplustot( terminal)
print('tots='),
print( tots)
# tots= {0: 0, 1: 100, 2: 200, 3: 270, 4: 280, 5: 300}
tards={}
tards[terminal]= auplustot( terminal)
def auplustard( t) :
  if tards.has_key( t) :
    return tards[ t]
  else:
    x = tots[ terminal]
    for (a, b, ab) in arcs :
      assert( a != terminal)
      assert( b != source)
      if a==t :
        x = min( x, auplustard( b) - ab)
        tards[ t ] = x
        return tards[ t ]
auplustard(source)
print('tards='),
print(tards )
for (a,b,ab) in arcs :
  if auplustard(a)==auplustot(a) and auplustard(b)==auplustot(b) and ab==auplustot(b)-auplustot(a) :
    print( (a, b, ab)),
    print( 'est critique')