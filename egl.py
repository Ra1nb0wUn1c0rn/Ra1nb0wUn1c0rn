#█▀▄ #
import os


#CHESS#
def chess(isRulesApply=True,board=None):
    #SETUP#
    possibleLetters=("a","b","c","d","e","f","g","h")
    possibleNumbers=(1,2,3,4,5,6,7,8)
    ltn = {let: num for let, num in zip(possibleLetters,range(8))}
    PLAYING=True
    START = [["r","n","b","q","k","b","n","r"],["p","p","p","p","p","p","p","p"],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],["P","P","P","P","P","P","P","P"],["R","N","B","Q","K","B","N","R"]]
    pieces = {
        "K":["   ██   "," ██████ ","   ██   "," ██████ "],
        "Q":[" █ ██ █ "," █ ██ █ "," ▀████▀ "," ██████ "],
        "R":[" █▄██▄█ ","   ██   ","   ██   "," ██████ "],
        "B":["  ▄██▄  ","  ████  ","   ██   "," ██████ "],
        "N":[" ▄████  "," ▀▀███  ","   ███  "," ██████ "],
        "P":["  ████  ","  ▀██▀  ","   ██   "," ██████ "],
        "k":[" ██████ ","   ██   "," ██████ ","   ██   "],
        "q":[" ██████ "," ▄████▄ "," █ ██ █ "," █ ██ █ "],
        "r":[" ██████ ","   ██   ","   ██   "," █▀██▀█ "],
        "b":[" ██████ ","   ██   ","  ████  ","  ▀██▀  "],
        "n":[" ██████ ","   ███  "," ▄▄███  "," ▀████  "],
        "p":[" ██████ ","   ██   ","  ▄██▄  ","  ████  "],
        " ":["        ","        ","        ","        "]}

    #FUNCTIONS#

    def bprt(board,p):
        l="     A       B       C       D       E       F       G       H      \n\n"
        r=f"{l}\n"

        for rr in range(8):
            ll=0
            r+=f"  {p[board[rr][0]][ll]}{p[board[rr][1]][ll]}{p[board[rr][2]][ll]}{p[board[rr][3]][ll]}{p[board[rr][4]][ll]}{p[board[rr][5]][ll]}{p[board[rr][6]][ll]}{p[board[rr][7]][ll]}\n"
            ll=1
            r+=f"{rr+1} {p[board[rr][0]][ll]}{p[board[rr][1]][ll]}{p[board[rr][2]][ll]}{p[board[rr][3]][ll]}{p[board[rr][4]][ll]}{p[board[rr][5]][ll]}{p[board[rr][6]][ll]}{p[board[rr][7]][ll]} {rr+1}\n"
            ll=2
            r+=f"  {p[board[rr][0]][ll]}{p[board[rr][1]][ll]}{p[board[rr][2]][ll]}{p[board[rr][3]][ll]}{p[board[rr][4]][ll]}{p[board[rr][5]][ll]}{p[board[rr][6]][ll]}{p[board[rr][7]][ll]}\n"
            ll=3
            r+=f"  {p[board[rr][0]][ll]}{p[board[rr][1]][ll]}{p[board[rr][2]][ll]}{p[board[rr][3]][ll]}{p[board[rr][4]][ll]}{p[board[rr][5]][ll]}{p[board[rr][6]][ll]}{p[board[rr][7]][ll]}\n\n"

        return r+l


    def isMovePoss(mv,bd):
        piece = bd[int(mv[1])-1][ltn[mv[0]]]
        taking = bd[int(mv[3])-1][ltn[mv[2]]]
        r=True
        if not piece.lower() in ["p","r","n","b","q","k"]:
            r=False
        elif (mv[0]==mv[2]) and (mv[1]==mv[3]):
            r=False
        else:
            if (piece.lower() == "p"):
                if piece == "p":
                    if ((taking==" " and (int(mv[3])-int(mv[1]))==1) or (taking==" " and (int(mv[3])-int(mv[1]))==2 and int(mv[1])==2)) and (mv[0]==mv[2]):
                        r=True
                    elif (taking!=" " and (int(mv[3])-int(mv[1]))==1) and (abs(ltn[mv[0]] - ltn[mv[2]])==1):
                        r=True
                elif piece == "P":
                    if ((taking==" " and (int(mv[3])-int(mv[1]))==-1) or (taking==" " and (int(mv[3])-int(mv[1]))==-2 and int(mv[1])==7)) and (mv[0]==mv[2]):
                        r=True
                    elif (taking!=" " and (int(mv[3])-int(mv[1]))==-1) and (abs(ltn[mv[0]] - ltn[mv[2]])==1):
                        r=True
            elif piece.lower() == "r":
                print("ROOK")#REMOVE
                r=True
                if int(mv[1])==int(mv[3]):
                    print("moving in row")#REMOVE
                elif mv[0].lower()==mv[2].lower():
                    print("moving in column")#REMOVE
                    n=0 if int(mv[1]) > int(mv[3]) else abs(int(mv[1])-int(mv[3]))-1
                    for i in range(abs(int(mv[1])-int(mv[3]))):
                        plagt = bd[int(mv[1])+(n-i)][ltn(mv[0])]
                        if plagt != ' ':
                            r=False
                else:
                    r=False
            elif (piece.lower() == "n"):
                pass
            elif piece.lower() == "b":
                pass
            elif piece.lower() == "q":
                pass
            elif piece.lower() == "k":
                pass
            return r

    
    #MAIN LOOP#
    while PLAYING:
        #os.system("clear")
        board = START if board is None else board
        print(bprt(board,pieces))
        mv = input("> ")
        if mv[0] == "/":
            if mv[1].lower() == "x":
                PLAYING = False
            elif mv[1].lower() == "r":
                isRulesApply = (int(isRulesApply)+1)%2
        elif len(mv) == 4:
            if (mv[0].lower() in possibleLetters)and(mv[2].lower() in possibleLetters)and(int(mv[1]) in possibleNumbers)and(int(mv[3]) in possibleNumbers):
                if not isRulesApply:
                    board[int(mv[3])-1][ltn[mv[2]]] = board[int(mv[1])-1][ltn[mv[0]]]
                    board[int(mv[1])-1][ltn[mv[0]]] = " "
                else:
                    print(((int(mv[1])-1)-(int(mv[3])-1),(ltn[mv[0]])-(ltn[mv[2]])))
                    if isMovePoss(mv,board):
                        board[int(mv[3])-1][ltn[mv[2]]] = board[int(mv[1])-1][ltn[mv[0]]]
                        if ((board[int(mv[1])-1][ltn[mv[0]]] == 'p') and (mv[3] == "8"))or((board[int(mv[1])-1][ltn[mv[0]]] == 'P')and(mv[3] == "1")):
                            board[int(mv[3])-1][ltn[mv[2]]] = "q" if mv[3] == "8" else "Q"
                        
                        board[int(mv[1])-1][ltn[mv[0]]] = " "
                    else:
                        print("Impossible move, to disable rules type /r")
            else:
                print("INCORECT COMMAND")
                print("type /h for help")
        else:
            print("INCORECT COMMAND LENGHT")
            print("type /h for help")

if __name__ == '__main__':
    chess()
