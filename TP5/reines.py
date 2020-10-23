def createBoard(n):
  return [[ 0 for j in range (n)]for i in range (n)]

def displayBoard(board,n):
  for i in range (n):
    for j in range (n):
      print(board[i][j],end=' ')
    print()

def isSafe(board, lig,col,n):
  for j in range (col,-1,-1):
    if board[lig][j]==1:
      return False
  i=lig
  j=col
  while i>=0 and j>=0:
    if board[i][j]==1:
      return False
    i-=1
    j-=1
  i=lig
  j=col
  while i<n and j >=0:
    if board[i][j]==1:
      return False
    i+=1
    j-=1  
  return True

def nReines(board,col,n):
  if col >= n : 
    return True
  for i in range (n):
    if isSafe(board,i,col,n):
      board[i][col]=1
      if nReines(board,col+1,n):
        return True
      board[i][col]=0
  return False

n=8
chessboard = createBoard(n)
nReines(chessboard,0,n)
displayBoard(chessboard,n)