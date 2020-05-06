bord=['_','_','_','_','_','_','_','_','_']
cur_player='x'
gameon=True
winner= None
def show():
    print(bord[0],"|",bord[1],"|",bord[2])
    print(bord[3],"|",bord[4],"|",bord[5])
    print(bord[6],"|",bord[7],"|",bord[8])
def game():
    global cur_player
    print('________________________________')

    print("__WELCOME TO BONGS TIC TOCTOE___")
    print('________________________________')

    show()

    while gameon:
        turn(cur_player)
        gameover()
        flip()

    if winner=="x":
        print('___________________________')
        print('________X IS WINNER________')
    elif winner=="o":
        print('___________________________')

        print('______O IS WINNER______----')
    else:
        print('---------TIE------')

    print("---------(-_-) THNX FOR PLAYING(-_-)--------")

def turn(player):
    vall=True
    print('____________________________')

    while  vall:

        print("_________"+player+"'s turn_____")
        pos = input("_____enter the position from 1-9_____")
        while pos not in ['1','2','3','4','5','6','7','8','9']:
            pos = input("________enter the valid  position from 1-9_________")

        pos=int(pos)-1
        if bord[pos]=='_':
            vall=False
        else:
            print("_______sorry this place is taken .. try again____")

    bord[pos]=player
    show()
def gameover():
 win()
 tie()



def flip():
    global cur_player
    if cur_player=="x":
       cur_player="o"
    elif cur_player=="o":
        cur_player="x"
    return cur_player

def win():
  global winner
  rwin=row()
  cwin=col()
  dwin=diag()
  if rwin:
      winner=rwin
  elif cwin :
      winner=cwin
  elif dwin:
      winner=dwin
  else:
      winner=None

  return


def tie():
  global gameon
  if '_' not in bord:
      gameon=False
def row():
    global gameon
    row1=bord[0]==bord[1]==bord[2]!='_'
    row2=bord[3]==bord[4]==bord[5]!='_'
    row3=bord[6]==bord[7]==bord[8]!='_'
    if row1 or row2 or row3:
        gameon = False
    if row1:
        return  bord[0]
    elif row2:
        return bord[3]
    elif row3:
        return bord[6]

    return
def col():
    global gameon
    row1 = bord[0] == bord[3] == bord[6] != '_'
    row2 = bord[1] == bord[4] == bord[7] != '_'
    row3 = bord[2] == bord[5] == bord[8] != '_'
    if row1 or row2 or row3:
        gameon = False
    if row1:
        return bord[0]
    elif row2:
        return bord[1]
    elif row3:
        return bord[2]
    return
def diag():
    global gameon
    row1 = bord[0] == bord[4] == bord[8] != '_'
    row3 = bord[2] == bord[4] == bord[6] != '_'
    if row1 or row3:
        gameon = False
    if row1:
        return bord[0]

    elif row3:
        return bord[2]
    return


game()
