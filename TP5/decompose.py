class Paire():
  def __init__(self,tete,queue):
    self.h=tete
    self.t=queue

def cons(tete,queue):
  return Paire(tete,queue)

def decomposer(n):
  if n==0 : 
    return cons(0,None)
  return cons(decomposer(n//10),n%10)