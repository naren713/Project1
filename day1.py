board=["_","_","_",
       "_","_","_",
       "_","_","_",]

def display_board():
       print(board[0],"|",board[1],"|",board[2])
       print(board[3],"|",board[4],"|",board[5])
       print(board[6],"|",board[7],"|",board[8])

def Player1_turn():
       position=input('''Enter the position for 'X' (1-9): ''')
       position=int(position)-1
       board[position]="X"
       display_board()

def Player2_turn():
       position=input('''Enter the position for 'O' (1-9): ''')
       position=int(position)-1
       board[position]="O"
       display_board()

display_board()
game_still_going=0


def Check_for_Winner():
       check_rows()
       check_columns()
       check_diagionally()



def check_rows():
       if board[0]==board[1]==board[2]=="X" or board[0]==board[1]==board[2]=='O':
              global game_still_going
              game_still_going=1
              print(board[0]," is Winner")
       elif board[3]==board[4]==board[5]=='X' or board[3]==board[4]==board[5]=='O':
              game_still_going=1
              print(board[3]," is Winner")
       elif board[6]==board[7]==board[8]=='X' or board[6]==board[7]==board[8]=='O':
              game_still_going=1
              print(board[6]," is Winner")
       


def check_columns():
       if board[0]==board[3]==board[6]=='X' or board[0]==board[3]==board[6]=='O':
              global game_still_going
              game_still_going=1
              print(board[0]," is Winner")
       elif board[1]==board[4]==board[7]=="X" or board[1]==board[4]==board[7]=='O':
              game_still_going=1
              print(board[1]," is Winner")
       elif board[2]==board[5]==board[8]=='X' or board[2]==board[5]==board[8]=='O':
              game_still_going=1
              print(board[2]," is Winner")

def check_diagionally():
       if board[0]==board[4]==board[8]=='X' or board[0]==board[4]==board[8]=='O':
              global game_still_going
              game_still_going=1
              print(board[0]," is Winner")
       elif board[2]==board[4]==board[6]=='X' or board[2]==board[4]==board[6]=='O':
              game_still_going=1
              print(board[2]," is Winner")


while game_still_going == 0:
       Player1_turn()
       Check_for_Winner() 
       if game_still_going==1:
              break      
       Player2_turn()
       Check_for_Winner()
       if game_still_going==1:
              break

