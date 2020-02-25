g=[[0,0,0,0,0,4,6,7,0,],
   [0,0,9,2,0,0,8,0,1,],
   [0,0,7,6,1,3,0,4,9,],
   [0,5,0,1,0,0,2,8,4,],
   [0,1,0,0,0,0,3,9,6,],
   [4,9,6,8,0,0,0,5,0,],
   [3,0,0,0,6,1,0,2,0,],
   [0,8,5,4,0,0,0,6,0,],
   [9,0,0,0,7,8,0,0,0,]]


def display(bo):
    for i in (g):
        print(i)

def check_row(x,y,n):
    for i in range(len(g)):
        if g[x][i]==n:
            return False

def check_col(x,y,n):
    for i in range(len(g)):
        if g[i][y]==n:
            return False

def check_box(x,y,n):
    x1=(x//3)*3
    y1=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if g[x1+i][y1+j]==n:
                return False

def find_empty(bo):
    for x in range(len(bo)):
        for y in range(len(bo)):
            if bo[x][y]==0:
                return(x,y)
    return None

def solve(bo):   
    f=find_empty(bo)
    if not f:
        return True
    else:
        x,y=f

    for n in range(1,10):
        a=(check_row(x,y,n))
        b=(check_col(x,y,n))
        c=(check_box(x,y,n))
        if a==None and b==None and c==None:
            bo[x][y]=n
            if solve(bo):
                return True
            bo[x][y]=0
    return False
solve(g)
# display(g)


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

print_board(g)



