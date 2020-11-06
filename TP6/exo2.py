import random
def createTab(n):
    return[random.randint(1,n*5) for i in range(1,n+1)]

class Node:
  def __init__(self,key):
    self.val = key
    self.left = None
    self.right = None

def insert(bst,key):
  if bst == None : 
    return Node(key)
  if bst.val == key :
    return bst
  if bst.val < key :
    bst.right = insert(bst.right,key)
  else : 
    bst.left = insert(bst.left,key)
  return bst

def createTreeTab(t):
  bst = None
  for x in range (len(t)):
    bst = insert(bst,t[x])
  return bst

def inOrder(bst,liste):
  if bst == None : 
    return liste
  else : 
    inOrder(bst.left,(bst.value,inOrder(bst.right,liste)))

def inOrderPrint(bst):
  if bst != None:
    inOrderPrint(bst.left)
    print(bst.val)
    inOrderPrint(bst.right)

n = 10
t = createTab(n)
print('t avant tri :')
print(t)
arbre = createTreeTab(t)
print('apres tri:')
inOrderPrint(arbre)