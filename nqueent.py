def nqueen():
    n=4
    col =set()
    posdig= set()
    negdig= set()

    res=[]

    board=[['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
    
    
    def printboard(board):
        for x in board:
            print(x)
            
        print("....................")

    def backtrack(r):


        if r == n:
            res=(board)
            printboard(board)
    
        
        for c in range(n):
            if c in col or (r+c) in posdig or (r-c) in negdig:
                continue

            col.add(c)
            posdig.add(r+c)
            negdig.add(r-c)
            board[r][c]='q'
            
            backtrack(r+1)

            col.remove(c)
            posdig.remove(r+c)
            negdig.remove(r-c)
            board[r][c]='.'

    backtrack(0)

nqueen()


