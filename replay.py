import signal
import os
import sys
from time import sleep
from src.input import *
from src.village import *
from threading import Thread

n = len(sys.argv)
if n == 1:
    outputFileName = "replays/output#.txt"
    outputVersion = 1
    while os.path.isfile(outputFileName.replace("#", str(outputVersion))):
        outputVersion += 1
    outputVersion-=1
    outputFileName = outputFileName.replace("#", str(outputVersion))
    f=open(outputFileName,"r")
if n>1:
    outputFileName = "replays/output"+str(sys.argv[1])+".txt"
    f=open(outputFileName,"r")
    spee = 1
if n==3:
    spee = int(sys.argv[2])

def firstFunction(b,board):
    for i in range(len(b)):
        l = b[i].move(board)==0

def secondFunction(board,k,b):
    for i in range(1,5):
        pk=exec("board.c"+str(i)+".boom(board,k,b)")
    pass # cannon fire continue but only one time
 
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    os.system("clear")
    cursor=Get()
    board=board(34,130,15)
    set_buildings(0,board,1)
    board.no_of_buildings=11
    cursor.hide()
    k=king()
    k.health=100
    k.show_king(board)
    board.no_of_troops=16
    b=[]
    l=0
    bb=0
    speed=0.1
    while(1):
        print('\033[35;38H'+"   ")
        print('\033[35;38H'+str(k.health))
        print('\033[35;61H'+"  ")
        print('\033[35;61H'+str(board.no_of_buildings))
        p = f.read(1)
        sleep(speed/spee)
        if not p:
            break
        # print('\033[1;1H')'
        if p == '-':
            pass
        elif p=='q':
            os.system("clear")
            break
        elif p=='z':
            if(bb<15):
                b.append(Barbarians(1,board))
                bb+=1
            else:
                pass # not possible to add more than 15 barbarians
            # spawn on one point 
            # b.array(append)
            # b.show that one 
        elif p=='x':
            if(bb<15):
                b.append(Barbarians(2,board))
                sleep(0.1)
                bb+=1

            else:
                pass
            # spawn on two points
        elif p=='c':
            if(bb<15):
                bb+=1
                b.append(Barbarians(3,board))

            else:
                pass
            # spawn on three points
        elif p=='f':
            os.system('afplay ./src/sounds/power_up.mp3')
            s=Spell("Fire",board,k,b)
            speed=0.05
            # fire spell 
        elif p=='h':
            os.system('afplay ./src/sounds/coin.mp3')
            s=Spell("Health",board,k,b)
            # health spell
        elif p=='l':
            l= board.k.levi(board)
        else:
            l = k.move(p,board)
        if(board.no_of_buildings==0):
            os.system("clear")
            print("\033[1;5H"+"You won!")
            os.system('afplay ./src/sounds/win.mp3')
            break
        elif(board.no_of_troops==0):
            os.system("clear")
            print("\033[1;5H"+"You lost!")
            os.system('afplay ./src/sounds/game_over.mp3')
            break
        else:
            t1= Thread(target=firstFunction(b,board))
            t2= Thread(target=secondFunction(board,k,b))
            t1.start()
            t2.start()
    set_buildings(1,board)
    print('\033[35;38H'+"   ")
    print('\033[35;38H'+str(k.health))
os.system("clear")
cursor.show()
f.close()

