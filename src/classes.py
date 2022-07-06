import os
from time import sleep
rows = 34
columns = 130
frames = 15
class board():
    def __init__(self, rows , cols ,frames):
        self.no_of_buildings=11
        self._rows = rows
        self._cols = columns
        self._grid = ([['\033[31m'+ ' '+'\033[0m' for col in range(self._cols)]
                       for row in range(self._rows)])
        self.build=([['n' for col in range(self._cols)]
                       for row in range(self._rows)])
        # for its buidings 
        self.h1 = 0
        self.h2 = 0
        self.h3 = 0
        self.h4 = 0
        self.h5 = 0
        self.h6 = 0
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.c4 = 0
        self.t = 0
        self.w=0
        self.no_of_troops=16
        self.health=100
        self.set_spawning_points1x=0
        self.set_spawning_points1y=0
        self.set_spawning_points2x=0
        self.set_spawning_points2y=0
        self.set_spawning_points3x=0
        self.set_spawning_points3y=0

        for val in range(self._cols):
            self._grid[0][val] = '\033[31m'+ '▪️'+'\033[0m'
            self._grid[self._rows - 1][val] = '\033[31m'+'▪️'+'\033[0m'
            self.build[0][val]='w'
            self.build[self._rows - 1][val] = 'w'
        for val in range(self._rows):
            self._grid[val][0] = '\033[31m'+'▪️'+'\033[0m'
            self._grid[val][1] = '\033[31m'+'▪️'+'\033[0m'
            self._grid[val][self._cols - 1] = '\033[31m'+'▪️'+'\033[0m'
            self._grid[val][self._cols - 2] = '\033[31m'+'▪️'+'\033[0m'
            self.build[val][0]='w'
            self.build[val][self._cols-2]='w'
            self.build[val][self._cols-1]='w'
            self.build[val][1]='w'

    def get_grid(self, i , j):
        return self._grid[i][j]
        
    def change_grid(self, i , j,val):
        self._grid[i][j] = val

    def show_grid(game_back):
        output_str = ""+'\033[0m'
        for row in range(rows):
            for col in range(columns):
                    output_str += game_back.get_grid(row,col)
            output_str += '\n'
        arr = [1,2,3]
        output_str +='\033[37m'+"                     " +"King's Health = "
        output_str += str(arr[0])
        output_str += "     Buildings left"
        output_str += " = "
        output_str += str(game_back.no_of_buildings)
        output_str += "     "
        output_str += " "
        output_str += '\n'
        output_str += '\t\tS=spawning points\t\t'                         
        output_str += '\033[33m'+'■=wall\t\t\t'+'\033[0m'
        output_str += 'C=cannon\t\t\t'
        output_str += 'H=hut\t\t\n\n'
        output_str += '           \t\t\t\t^=starting point of king\t\t'
        output_str += 'TH=townhall'+'\033[0m'
        print('\033[H' + output_str+'\033[0m')
    
    def show_build(game_back):
        output_str = ""+'\033[0m'
        for row in range(rows):
            for col in range(columns):
                    output_str += game_back.build[row][col]+" "+str(row)+" "+str(col)+" "
            output_str += '\n'
        print('\033[H' + output_str+'\033[0m')

    def set_spawning_point(self, a,b,c,d,e,f):
        self.change_grid(0,64,'\033[37m'+' '+'\033[0m')
        self.change_grid(33,64,'\033[37m'+' '+'\033[0m')
        self.change_grid(33,65,'\033[37m'+'^'+'\033[0m')
        self.change_grid(33,66,'\033[37m'+'^'+'\033[0m')

        self.change_grid(a+2,b-2,'\033[37m'+'S'+'\033[0m')
        self.change_grid(a+2,b-1,'\033[37m'+'S'+'\033[0m')
        self.change_grid(e+2,f+2,'\033[37m'+'S'+'\033[0m')
        self.change_grid(e+2,f+1,'\033[37m'+'S'+'\033[0m')
        self.change_grid(a+2+1,b-2,'\033[37m'+'S'+'\033[0m')
        self.change_grid(a+2+1,b-1,'\033[37m'+'S'+'\033[0m')
        self.change_grid(e+2+1,f+2,'\033[37m'+'S'+'\033[0m')
        self.change_grid(e+2+1,f+1,'\033[37m'+'S'+'\033[0m')
        self.change_grid(c-1,d+2,'\033[37m'+'S'+'\033[0m')
        self.change_grid(c-1,d+3,'\033[37m'+'S'+'\033[0m')
        

        self.build[a+2][b-2]='s'
        self.build[a+2][b-1]='s'
        self.build[e+2][f+2]='s'
        self.build[e+2][f+1]='s'
        self.build[a+2+1][b-2]='s'
        self.build[a+2+1][b-1]='s'
        self.build[e+2+1][f+2]='s'
        self.build[e+2+1][f+1]='s'
        self.build[c-1][d+2]='s'
        self.build[c-1][d+3]='s'

        self.build[0][64]='s'
        self.build[33][64]='s'
        self.build[33][65]='s'
        self.build[33][66]='s'

    def game_over(self,i):
        return i

def send_color(health):
    if health>60:
        s='\033[32m' 
    elif health>30:
        s='\033[33m'
    elif health>0:
        s='\033[31m'
    else:
        s='\033[37m'
    return s

class building:
    def __init__(self) -> None:
        self.health = 100
        self.x=0
        self.y=0
        self.k=0
    
class hut(building):
    def set_hut(self,i,j,game_back):
        self.x=i-2
        self.y=j-2
        s=send_color(self.health)
        game_back.change_grid(i-3,j-1,'\033[37m'+'H'+'\033[0m')
        game_back.build[i-3][j-1]='h'+str(self.k)
        for p in range(i-2,i):
            for q in range(j-2,j):
                game_back.change_grid(p,q,s+'⬤'+'\033[0m')
                game_back.build[p][q]='h'+str(self.k)
                print("\033["+str(p+1)+";"+str(q+1)+"H"+s+'⬤'+'\033[0m')

    def remove(self,i,j,game_back):
        game_back.change_grid(i-3,j-1,'\033[31m \033[0m')
        game_back.build[i-3][j-1]='n'
        print("\033["+str(i-2)+";"+str(j)+"H"+'\033[31m \033[0m')
        for p in range(i-2,i):
            for q in range(j-2,j):
                game_back.change_grid(p,q,'\033[31m'+ ' '+'\033[0m')
                game_back.build[p][q]='n'
                print("\033["+str(p+1)+";"+str(q+1)+"H"+'\033[31m \033[0m')

    def changehealth(self,game_back,i) -> None:
        self.health-=i
        self.set_hut(self.x +2,self.y +2,game_back)
        if self.health==0:
            self.remove(self.x +2,self.y +2,game_back)

class TH(building):
    def set_TH(self,game_back):
        self.x=14
        self.y=63
        s=send_color(self.health)    
        for p in range(14,18):
            for q in range(63,69):
                game_back.change_grid(p,q,s+'⬤'+'\033[0m')
                game_back.build[p][q]='t'
                print("\033["+str(p+1)+";"+str(q+1)+"H"+s+'⬤'+'\033[0m')
        for p in range(15,17):
                game_back.change_grid(p,65,'\033[37m'+'T'+'\033[0m')
                game_back.build[p][65]='t'
                print("\033["+str(p+1)+";"+str(65+1)+"H"+'T'+'\033[0m')
                game_back.change_grid(p,66,'\033[37m'+'H'+'\033[0m')
                game_back.build[p][66]='t'
                print("\033["+str(p+1)+";"+str(67)+"H"+'H'+'\033[0m')

    def remove_TH(self,game_back):
        for p in range(14,18):
            for q in range(63,69):
                game_back.change_grid(p,q,'\033[31m'+ ' '+'\033[0m')
                game_back.build[p][q]='n'
                print("\033["+str(p+1)+";"+str(q+1)+"H"+'\033[31m \033[0m')
        for p in range(15,17):
                game_back.change_grid(p,65,'\033[31m'+ ' '+'\033[0m')
                game_back.build[p][65]='n'
                print("\033["+str(p+1)+";"+str(65+1)+"H"+'\033[31m \033[0m')
                game_back.change_grid(p,66,'\033[31m'+ ' '+'\033[0m')
                game_back.build[p][66]='n'
                print("\033["+str(p+1)+";"+str(67)+"H"+'\033[31m \033[0m')

    def changehealth(self,game_back,i) -> None:
        self.health-=i
        self.set_TH(game_back)
        if self.health==0:
            self.remove_TH(game_back)

class cannon(building):
    def __init__(self) -> None:
        self.damageb=10
        self.damagek=10
        self.health=100

    def set_cannon(self,i,j,game_back):
        self.x=i-2
        self.y=j-2
        s=send_color(self.health)    
        game_back.change_grid(i-3,j-1,'\033[37m'+'C'+'\033[0m')
        game_back.build[i-3][j-1]='c'+str(self.k)
        for p in range(i-2,i):
            for q in range(j-2,j):
                game_back.change_grid(p,q,'\033[32m'+'⬤'+'\033[0m')
                game_back.build[p][q]='c'+str(self.k)
                print("\033["+str(p+1)+";"+str(q+1)+"H"+s+'⬤'+'\033[0m')

    def remove(self,i,j,game_back):
        game_back.change_grid(i-3,j-1,'\033[31m \033[0m')
        game_back.build[i-3][j-1]='n'
        print("\033["+str(i-2)+";"+str(j)+"H"+'\033[31m \033[0m')
        for p in range(i-2,i):
            for q in range(j-2,j):
                game_back.change_grid(p,q,'\033[31m'+ ' '+'\033[0m')
                game_back.build[p][q]='n'
                print("\033["+str(p+1)+";"+str(q+1)+"H"+'\033[31m \033[0m')

    def changehealth(self,game_back,i) -> None:
        self.health-=i
        self.set_cannon(self.x +2,self.y +2,game_back)
        if self.health==0:
            self.remove(self.x +2,self.y +2,game_back)
    
    def boom(self,game_back,k,b):
        if self.health>0:
            pq_var=0
            for i in range(self.x-3,self.x+4):
                if (pq_var==1):
                    break
                for j in range(self.y-3,self.y+4):
                    # print("\033["+str(i+1)+";"+str(j+1)+"H"+game_back.build[i][j]+'\033[0m')
                    if game_back.build[i][j]=='k':
                        k.changehealth(game_back,2)
                        pq_var=1
                    elif game_back.build[i][j]=='b':
                        for k in range(len(b)):
                            if b[k].x==i and b[k].y==j:
                                b[k].changehealth(game_back,100)
                                break
                        pq_var=1
        else:
            pass
        
class wall():
    def set_wall(self,i,j,k,l,game_back) -> None:
        for q in range(j,l):
            game_back.change_grid(i,q,'\033[33m'+'■'+'\033[0m')
            game_back.build[i][q]='w'
            game_back.change_grid(k,q,'\033[33m'+'■'+'\033[0m')
            game_back.build[k][q]='w'
        for p in range(i,k):
            game_back.change_grid(p,l,'\033[33m'+'■'+'\033[0m')
            game_back.build[p][l]='w'
            game_back.change_grid(p,l+1,'\033[33m'+'■'+'\033[0m')
            game_back.build[p][l+1]='w'
            game_back.change_grid(p,j,'\033[33m'+'■'+'\033[0m')
            game_back.build[p][j]='w'
            game_back.change_grid(p,j+1,'\033[33m'+'■'+'\033[0m')
            game_back.build[p][j+1]='w'
        game_back.change_grid(k,l,'\033[33m'+'■'+'\033[0m')
        game_back.build[k][l]='w'
        game_back.change_grid(k,l+1,'\033[33m'+'■'+'\033[0m')
        game_back.build[k][l+1]='w'

class king():
    def __init__(self) -> None:
        self.health=300
        self.x=23 #32
        self.y=66
        self.damageall=25
        self.damageTH=10
        self.movement=1
    
    def show_king(self,game_back):
        print("\033["+str(self.x)+";"+str(self.y)+"H"+"K"+'\033[0m')
        print("\033["+str(self.x)+";"+str(self.y+1)+"H"+"K"+'\033[0m')
        game_back.change_grid(self.x-1,self.y,'\033[33m'+'K'+'\033[0m')
        game_back.build[self.x-1][self.y]='k'
        game_back.change_grid(self.x-1,self.y-1,'\033[33m'+'K'+'\033[0m')
        game_back.build[self.x-1][self.y-1]='k'
    
    def remove(self,game_back):
        game_back.change_grid(self.x-1,self.y-1,'\033[31m \033[0m')
        game_back.build[self.x-1][self.y]='n'
        game_back.change_grid(self.x-1,self.y,'\033[31m \033[0m')
        game_back.build[self.x][self.y+1]='n'
        print("\033["+str(self.x)+";"+str(self.y)+"H"+'\033[31m \033[0m')
        print("\033["+str(self.x)+";"+str(self.y+1)+"H"+'\033[31m \033[0m')

    def move(self,s,game_back):
        if s=='w' or s=='W':
            if game_back._grid[self.x-2][self.y-1]=='\033[31m \033[0m' and game_back._grid[self.x-2][self.y]=='\033[31m \033[0m':
                print("\033["+str(self.x)+";"+str(self.y)+"H"+" ")
                print("\033["+str(self.x)+";"+str(self.y+1)+"H"+" ")
                game_back.change_grid(self.x-1,self.y,'\033[31m'+' '+'\033[0m')
                game_back.build[self.x-1][self.y]='n'
                game_back.change_grid(self.x-1,self.y-1,'\033[31m'+' '+'\033[0m')
                game_back.build[self.x-1][self.y-1]='n'
                self.x-=1
                self.show_king(game_back)
        elif s=='a' or s=='A':
            if game_back._grid[self.x-1][self.y-2]=='\033[31m \033[0m' :
                print("\033["+str(self.x)+";"+str(self.y+1)+"H"+" "+'\033[0m')
                game_back.change_grid(self.x-1,self.y,'\033[31m'+' '+'\033[0m')
                game_back.build[self.x-1][self.y]='n'
                self.y-=1
                self.show_king(game_back)
        elif s=='s' or s=='S':
            if game_back._grid[self.x][self.y-1]=='\033[31m \033[0m' and game_back._grid[self.x][self.y]=='\033[31m \033[0m':
                print("\033["+str(self.x)+";"+str(self.y)+"H"+" ")
                print("\033["+str(self.x)+";"+str(self.y+1)+"H"+" ")
                game_back.change_grid(self.x-1,self.y,'\033[31m'+' '+'\033[0m')
                game_back.build[self.x-1][self.y]='n'
                game_back.change_grid(self.x-1,self.y-1,'\033[31m'+' '+'\033[0m')
                game_back.build[self.x-1][self.y-1]='n'
                self.x+=1
                self.show_king(game_back)
        elif s=='d' or s=='D':
            if game_back._grid[self.x-1][self.y+1]=='\033[31m \033[0m' :
                print("\033["+str(self.x)+";"+str(self.y)+"H"+" "+'\033[0m')
                game_back.change_grid(self.x-1,self.y-1,'\033[31m'+' '+'\033[0m')
                game_back.build[self.x-1][self.y-1]='n'
                self.y+=1
                self.show_king(game_back)
        if(self.movement==2):
            if s=='w' or s=='W':
                if game_back._grid[self.x-2][self.y-1]=='\033[31m \033[0m' and game_back._grid[self.x-2][self.y]=='\033[31m \033[0m':
                    print("\033["+str(self.x)+";"+str(self.y)+"H"+" ")
                    print("\033["+str(self.x)+";"+str(self.y+1)+"H"+" ")
                    game_back.change_grid(self.x-1,self.y,'\033[31m'+' '+'\033[0m')
                    game_back.build[self.x-1][self.y]='n'
                    game_back.change_grid(self.x-1,self.y-1,'\033[31m'+' '+'\033[0m')
                    game_back.build[self.x-1][self.y-1]='n'
                    self.x-=1
                    self.show_king(game_back)
            elif s=='a' or s=='A':
                if game_back._grid[self.x-1][self.y-2]=='\033[31m \033[0m' :
                    print("\033["+str(self.x)+";"+str(self.y+1)+"H"+" "+'\033[0m')
                    game_back.change_grid(self.x-1,self.y,'\033[31m'+' '+'\033[0m')
                    game_back.build[self.x-1][self.y]='n'
                    self.y-=1
                    self.show_king(game_back)
            elif s=='s' or s=='S':
                if game_back._grid[self.x][self.y-1]=='\033[31m \033[0m' and game_back._grid[self.x][self.y]=='\033[31m \033[0m':
                    print("\033["+str(self.x)+";"+str(self.y)+"H"+" ")
                    print("\033["+str(self.x)+";"+str(self.y+1)+"H"+" ")
                    game_back.change_grid(self.x-1,self.y,'\033[31m'+' '+'\033[0m')
                    game_back.build[self.x-1][self.y]='n'
                    game_back.change_grid(self.x-1,self.y-1,'\033[31m'+' '+'\033[0m')
                    game_back.build[self.x-1][self.y-1]='n'
                    self.x+=1
                    self.show_king(game_back)
            elif s=='d' or s=='D':
                if game_back._grid[self.x-1][self.y+1]=='\033[31m \033[0m' :
                    print("\033["+str(self.x)+";"+str(self.y)+"H"+" "+'\033[0m')
                    game_back.change_grid(self.x-1,self.y-1,'\033[31m'+' '+'\033[0m')
                    game_back.build[self.x-1][self.y-1]='n'
                    self.y+=1
                    self.show_king(game_back)
        elif s==' ':
            return self.hit(game_back)
        return 0

    def hitlol(self,pp,game_back):
        if(pp.health>0):
                pp.changehealth(game_back,self.damageall)
                if pp.health<=0 :
                    pp.remove(pp.x+2,pp.y+2,game_back)
                    game_back.no_of_buildings-=1
                    if(game_back.no_of_buildings<=0):
                        return game_back.game_over(1)
                return 0

    def hit(self,game_back):
        x=self.x
        y=self.y
        for i in range(x-2,x+1):
            for j in range(y-2,y+2):
                if (i==x-2 and j==y-2) or (i==x-2 and j==y+1) or (i==x and j==y-2) or (i==x and j==y+1) :
                    continue
                if game_back.build[i][j][0]=='h':
                    if game_back.build[i][j][1]=='1' :
                        return self.hitlol(game_back.h1,game_back) 
                    elif game_back.build[i][j][1]=='2' :
                        return self.hitlol(game_back.h2,game_back)
                    elif game_back.build[i][j][1]=='3' :
                        return self.hitlol(game_back.h3,game_back)
                    elif game_back.build[i][j][1]=='4' :
                        return self.hitlol(game_back.h4,game_back)
                    elif game_back.build[i][j][1]=='5' :
                        return self.hitlol(game_back.h5,game_back)
                    elif game_back.build[i][j][1]=='6' :
                        return self.hitlol(game_back.h6,game_back)
                elif game_back.build[i][j][0]=='c' :
                    if game_back.build[i][j][1]=='1' :
                        return self.hitlol(game_back.c1,game_back)
                    elif game_back.build[i][j][1]=='2' :
                        return self.hitlol(game_back.c2,game_back)
                    elif game_back.build[i][j][1]=='3' :
                        return self.hitlol(game_back.c3,game_back)
                    elif game_back.build[i][j][1]=='4' :
                        return self.hitlol(game_back.c4,game_back)
                elif game_back.build[i][j][0]=='t' :
                    game_back.t.changehealth(game_back,self.damageTH)
                    if game_back.t.health<=0 :
                        game_back.t.remove_TH(game_back)
                        game_back.no_of_buildings-=1
                        if(game_back.no_of_buildings<=0):
                            return game_back.game_over(1)
                    return 0
        if(game_back.build[x-2][y-1]=='w'):
            game_back.build[x-2][y-1]='n'
            game_back.change_grid(x-2,y-1,'\033[31m'+' '+'\033[0m')
            print("\033["+str(x-1)+";"+str(y)+"H"+" "+'\033[0m')
            if(game_back.build[x-2][y]=='w'):
                game_back.build[x-2][y]='n'
                game_back.change_grid(x-2,y,'\033[31m'+' '+'\033[0m')
                print("\033["+str(x-1)+";"+str(y+1)+"H"+" "+'\033[0m')
            return 0
        elif(game_back.build[x-2][y]=='w'):
            game_back.build[x-2][y]='n'
            game_back.change_grid(x-2,y,'\033[31m'+' '+'\033[0m')
            print("\033["+str(x-1)+";"+str(y+1)+"H"+" "+'\033[0m')
        elif(game_back.build[x-1][y-2]=='w'):
            game_back.build[x-1][y-2]='n'
            game_back.change_grid(x-1,y-2,'\033[31m'+' '+'\033[0m')
            print("\033["+str(x)+";"+str(y-1)+"H"+" "+'\033[0m')
            if(game_back.build[x-1][y-3]=='w'):
                game_back.build[x-1][y-3]='n'
                game_back.change_grid(x-1,y-3,'\033[31m'+' '+'\033[0m')
                print("\033["+str(x)+";"+str(y-2)+"H"+" "+'\033[0m')
        elif(game_back.build[x-1][y+1]=='w'):
            game_back.build[x-1][y+1]='n'
            game_back.change_grid(x-1,y+1,'\033[31m'+' '+'\033[0m')
            print("\033["+str(x)+";"+str(y+2)+"H"+" "+'\033[0m')
            if(game_back.build[x-1][y+2]=='w'):
                game_back.build[x-1][y+2]='n'
                game_back.change_grid(x-1,y+2,'\033[31m'+' '+'\033[0m')
                print("\033["+str(x)+";"+str(y+3)+"H"+" "+'\033[0m')
        if(game_back.build[x][y-1]=='w'):
            game_back.build[x][y-1]='n'
            game_back.change_grid(x,y-1,'\033[31m'+' '+'\033[0m')
            print("\033["+str(x+1)+";"+str(y)+"H"+" "+'\033[0m')
            if(game_back.build[x][y]=='w'):
                game_back.build[x][y]='n'
                game_back.change_grid(x,y,'\033[31m'+' '+'\033[0m')
                print("\033["+str(x+1)+";"+str(y+1)+"H"+" "+'\033[0m')
            return 0
        elif(game_back.build[x][y]=='w'):
            game_back.build[x][y]='n'
            game_back.change_grid(x,y,'\033[31m'+' '+'\033[0m')
            print("\033["+str(x+1)+";"+str(y+1)+"H"+" "+'\033[0m')

    def changehealth(self,game_back,damage):
        if self.health>0 :
            self.health-=damage
            game_back.health=self.health
            if self.health<=0 :
                game_back.no_of_troops-=1
        if self.health<=0:
            self.remove(game_back)        

    def levi(self,game_back):
        x=self.x
        y=self.y
        for i in range(x-5,x+5):
            for j in range(y-7,y+7):
                if game_back.build[i][j][0]=='h':
                    if len(game_back.build[i][j])==2 and game_back.build[i][j][1]=='1' :
                        self.hitlol(game_back.h1,game_back) 
                    if len(game_back.build[i][j])==2 and game_back.build[i][j][1]=='2' :
                        self.hitlol(game_back.h2,game_back)
                    if len(game_back.build[i][j])==2 and game_back.build[i][j][1]=='3' :
                        self.hitlol(game_back.h3,game_back)
                    if len(game_back.build[i][j])==2 and game_back.build[i][j][1]=='4' :
                        self.hitlol(game_back.h4,game_back)
                    if len(game_back.build[i][j])==2 and game_back.build[i][j][1]=='5' :
                        self.hitlol(game_back.h5,game_back)
                    if len(game_back.build[i][j])==2 and game_back.build[i][j][1]=='6' :
                        self.hitlol(game_back.h6,game_back)
                if game_back.build[i][j][0]=='c' :
                    if len(game_back.build[i][j])==2 and game_back.build[i][j][1]=='1' :
                        self.hitlol(game_back.c1,game_back)
                    if len(game_back.build[i][j])==2 and game_back.build[i][j][1]=='2' :
                        self.hitlol(game_back.c2,game_back)
                    if len(game_back.build[i][j])==2 and game_back.build[i][j][1]=='3' :
                        self.hitlol(game_back.c3,game_back)
                    if len(game_back.build[i][j])==2 and game_back.build[i][j][1]=='4' :
                        self.hitlol(game_back.c4,game_back)
                if game_back.build[i][j][0]=='t' :
                    game_back.t.changehealth(game_back,self.damageTH)
                    if game_back.t.health<=0 :
                        game_back.t.remove_TH(game_back)
                        game_back.no_of_buildings-=1
                        if(game_back.no_of_buildings<=0):
                            return game_back.game_over(1)
                if game_back.build[i][j]=='w' :
                    game_back.build[i][j]='n'
                    game_back.change_grid(i,j,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(i+1)+";"+str(j+1)+"H"+" "+'\033[0m')
        
class Barbarians():
    def __init__(self,i,game_back):
        # make one array that to use this and for each element of the array store time and the spawning points 
        self.health=5000
        self.damageTH=1
        self.damageall=2
        if(i==1):
            self.x=game_back.set_spawning_points1x
            self.y=game_back.set_spawning_points1y
        if(i==2):
            self.x=game_back.set_spawning_points2x
            self.y=game_back.set_spawning_points2y # position two
        if(i==3):
            self.x=game_back.set_spawning_points3x
            self.y=game_back.set_spawning_points3y # position three
        game_back.build[self.x][self.y]='b'
        game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')

    def remove(self,game_back):
        
        game_back.change_grid(self.x,self.y,'\033[31m \033[0m')
        game_back.build[self.x][self.y]='n'
        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m \033[0m')        

    def hitlol(self,pp,game_back):
        if(pp.health>0):
                pp.changehealth(game_back,self.damageall)
                if pp.health<=0 :
                    pp.remove(pp.x+2,pp.y+2,game_back)
                    game_back.no_of_buildings-=1
                    if(game_back.no_of_buildings<=0):
                        return game_back.game_over(1)
                return 0
   
    def hit(self,game_back):
        o=0
        # print("\033[2;1H"+str(self.x)+" "+str(self.y)+" "+'\033[0m')
        for k in range(self.x-1,self.x+2):
                for l in range(self.y-1,self.y+2):
                    o+=1
                    i=k
                    j=l
                    # print("\033["+str(o)+";1H"+game_back.build[i][j]+" "+str(i)+" "+str(j)+" "+'\033[0m')
                    if(len(game_back.build[i][j])==2):
                        if game_back.build[i][j][0]=='h':
                            if game_back.build[i][j][1]=='1' :
                                return self.hitlol(game_back.h1,game_back) 
                            elif game_back.build[i][j][1]=='2' :
                                return self.hitlol(game_back.h2,game_back)
                            elif game_back.build[i][j][1]=='3' :
                                return self.hitlol(game_back.h3,game_back)
                            elif game_back.build[i][j][1]=='4' :
                                return self.hitlol(game_back.h4,game_back)
                            elif game_back.build[i][j][1]=='5' :
                                return self.hitlol(game_back.h5,game_back)
                            elif game_back.build[i][j][1]=='6' :
                                return self.hitlol(game_back.h6,game_back)
                        elif game_back.build[i][j][0]=='c' :
                            if game_back.build[i][j][1]=='1' :
                                return self.hitlol(game_back.c1,game_back)
                            elif game_back.build[i][j][1]=='2' :
                                return self.hitlol(game_back.c2,game_back)
                            elif game_back.build[i][j][1]=='3' :
                                return self.hitlol(game_back.c3,game_back)
                            elif game_back.build[i][j][1]=='4' :
                                return self.hitlol(game_back.c4,game_back)
                    elif game_back.build[i][j]=='t' :
                        game_back.t.changehealth(game_back,self.damageTH)
                        if game_back.t.health<=0 :
                            game_back.t.remove_TH(game_back)
                            game_back.no_of_buildings-=1
                            if(game_back.no_of_buildings<=0):
                                return game_back.game_over(1)
                        return 0

    def move(self,game_back):
            # print(self.health)
        print("\033[1;1H"+str(self.health))
        # print("\033[1;1H"+self.health)
        pq=0
        if(self.health>0): 
            pq=1   
            mi=200
            m=[0,0]
            no=0
            p=[[7,33,game_back.h1.health],[17,33,game_back.h2.health],[27,33,game_back.h3.health],[7,99,game_back.h4.health],[17,99,game_back.h5.health],[27,99,game_back.h6.health],[15,65,game_back.t.health],[11,44,game_back.c1.health],[23,44,game_back.c2.health],[11,88,game_back.c3.health],[23,88,game_back.c4.health]]
            for i in range(0,len(p)):
                if(p[i][2]>0):
                    if abs(abs(p[i][0]-self.x)+abs(p[i][1]-self.y))<mi:
                        mi=abs(abs(p[i][0]-self.x)+abs(p[i][1]-self.y))
                        m=list(p[i][0:2])
                        no=i
            x=self.x
            y=self.y
            if no==6:
                i=14
                j=63
                p=5
                q=3
            else:
                i=m[0]-2
                j=m[1]-2
                p=1
                q=1
            if no>6:
                self.changehealth(game_back,50)
            if x<=i and y<=j:
                if(game_back._grid[x+1][y+1]=='\033[31m'+' '+'\033[0m'):
                    game_back.build[self.x][self.y]='n'
                    game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                    self.x+=1
                    self.y+=1
                    game_back.build[self.x][self.y]='b'
                    game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                    #sleep(0.05)
                if(game_back._grid[x+1][y+1]=='\x1b[33m■\x1b[0m'):
                    game_back.build[x+1][y+1]='n'
                    game_back.change_grid(x+1,y+1,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(x+2)+";"+str(y+2)+"H"+'\033[31m'+' '+'\033[0m')
                    #sleep(0.05)
            elif x<=i and y>=j+p:
                if(game_back._grid[x+1][y-1]=='\033[31m'+' '+'\033[0m'):
                    game_back.build[self.x][self.y]='n'
                    game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                    self.x+=1
                    self.y-=1
                    game_back.build[self.x][self.y]='b'
                    game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                    #sleep(0.05)
                if(game_back._grid[x+1][y-1]=='\x1b[33m■\x1b[0m'):
                    game_back.build[x+1][y-1]='n'
                    game_back.change_grid(x+1,y-1,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(x+2)+";"+str(y)+"H"+'\033[31m'+' '+'\033[0m')
                    #sleep(0.05)
            elif x>=i+q and y<=j:
                if(game_back._grid[x-1][y+1]=='\033[31m'+' '+'\033[0m'):
                    game_back.build[self.x][self.y]='n'
                    game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                    self.x-=1
                    self.y+=1
                    game_back.build[self.x][self.y]='b'
                    game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                    #sleep(0.05)
                if(game_back._grid[x-1][y+1]=='\x1b[33m■\x1b[0m'):
                    game_back.build[x-1][y+1]='n'
                    game_back.change_grid(x-1,y+1,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(x)+";"+str(y+2)+"H"+'\033[31m'+' '+'\033[0m')
                    #sleep(0.05)
            elif x>=i+q and y>=j+p:
                if(game_back._grid[x-1][y-1]=='\033[31m'+' '+'\033[0m'):
                    game_back.build[self.x][self.y]='n'
                    game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                    self.x-=1
                    self.y-=1
                    game_back.build[self.x][self.y]='b'
                    game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                    #sleep(0.05)
                if(game_back._grid[x-1][y-1]=='\x1b[33m■\x1b[0m'):
                    game_back.build[x-1][y-1]='n'
                    game_back.change_grid(x-1,y-1,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(x)+";"+str(y)+"H"+'\033[31m'+' '+'\033[0m')
                    #sleep(0.05)
            elif no==6:
                if(x==15 and y<j) or (y==64 or 65 and x<i):
                    if(game_back._grid[x+1][y+1]=='\x1b[33m■\x1b[0m'):
                        game_back.build[x+1][y+1]='n'
                        game_back.change_grid(x+1,y+1,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(x+2)+";"+str(y+2)+"H"+'\033[31m'+' '+'\033[0m')
                        #sleep(0.05)
                    if(game_back._grid[x+1][y+1]=='\033[31m'+' '+'\033[0m'):
                        game_back.build[self.x][self.y]='n'
                        game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                        self.x+=1
                        self.y+=1
                        game_back.build[self.x][self.y]='b'
                        game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')    
                elif(x==15 and y>j) or (y==67 or 66 and x<i):
                    if(game_back._grid[x+1][y-1]=='\x1b[33m■\x1b[0m'):
                        game_back.build[x+1][y-1]='n'
                        game_back.change_grid(x+1,y-1,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(x+2)+";"+str(y)+"H"+'\033[31m'+' '+'\033[0m')
                        #sleep(0.05)
                    if(game_back._grid[x+1][y-1]=='\033[31m'+' '+'\033[0m'):
                        game_back.build[self.x][self.y]='n'
                        game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                        self.x+=1
                        self.y-=1
                        game_back.build[self.x][self.y]='b'
                        game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                elif(x==16 and y<j) or (y==64 or 65 and x>i+q):
                    if(game_back._grid[x-1][y+1]=='\x1b[33m■\x1b[0m'):
                        game_back.build[x-1][y+1]='n'
                        game_back.change_grid(x-1,y+1,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(x)+";"+str(y+2)+"H"+'\033[31m'+' '+'\033[0m')
                        #sleep(0.05)
                    if(game_back._grid[x-1][y+1]=='\033[31m'+' '+'\033[0m'):
                        game_back.build[self.x][self.y]='n'
                        game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                        self.x-=1
                        self.y+=1
                        game_back.build[self.x][self.y]='b'
                        game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                elif(x==16 and y>j) or (y==67 or 66 and x>i+q):
                    if(game_back._grid[x-1][y-1]=='\x1b[33m■\x1b[0m'):
                        game_back.build[x-1][y-1]='n'
                        game_back.change_grid(x-1,y-1,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(x)+";"+str(y)+"H"+'\033[31m'+' '+'\033[0m')
                        #sleep(0.05)
                    if(game_back._grid[x-1][y-1]=='\033[31m'+' '+'\033[0m'):
                        game_back.build[self.x][self.y]='n'
                        game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                        self.x-=1
                        self.y-=1
                        game_back.build[self.x][self.y]='b'
                        game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
            return self.hit(game_back)
        if (pq==0):
            self.remove(game_back)
    def changehealth(self,game_back,damage):
        # sleep(0.05)
        if self.health>0 :
            self.health-=damage
            if self.health<=0 :
                game_back.no_of_troops-=1
                self.remove(game_back)
    
class Archers():
    def __init__(self,i,game_back):
        # make one array that to use this and for each element of the array store time and the spawning points 
        self.health=100
        self.damageTH=1
        self.damageall=2
        if(i==1):
            self.x=game_back.set_spawning_points1x
            self.y=game_back.set_spawning_points1y
        if(i==2):
            self.x=game_back.set_spawning_points2x
            self.y=game_back.set_spawning_points2y # position two
        if(i==3):
            self.x=game_back.set_spawning_points3x
            self.y=game_back.set_spawning_points3y # position three
        game_back.build[self.x][self.y]='b'
        game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')

    def remove(self,game_back):
        game_back.change_grid(self.x,self.y,'\033[31m \033[0m')
        game_back.build[self.x][self.y]='n'
        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m \033[0m')        

    def hitlol(self,pp,game_back):
        if(pp.health>0):
                pp.changehealth(game_back,self.damageall)
                if pp.health<=0 :
                    pp.remove(pp.x+2,pp.y+2,game_back)
                    game_back.no_of_buildings-=1
                    if(game_back.no_of_buildings<=0):
                        return game_back.game_over(1)
                return 0
   
    def hit(self,game_back):
        o=0
        # print("\033[2;1H"+str(self.x)+" "+str(self.y)+" "+'\033[0m')
        for k in range(self.x-1,self.x+2):
                for l in range(self.y-1,self.y+2):
                    o+=1
                    i=k
                    j=l
                    # print("\033["+str(o)+";1H"+game_back.build[i][j]+" "+str(i)+" "+str(j)+" "+'\033[0m')
                    if(len(game_back.build[i][j])==2):
                        if game_back.build[i][j][0]=='h':
                            if game_back.build[i][j][1]=='1' :
                                return self.hitlol(game_back.h1,game_back) 
                            elif game_back.build[i][j][1]=='2' :
                                return self.hitlol(game_back.h2,game_back)
                            elif game_back.build[i][j][1]=='3' :
                                return self.hitlol(game_back.h3,game_back)
                            elif game_back.build[i][j][1]=='4' :
                                return self.hitlol(game_back.h4,game_back)
                            elif game_back.build[i][j][1]=='5' :
                                return self.hitlol(game_back.h5,game_back)
                            elif game_back.build[i][j][1]=='6' :
                                return self.hitlol(game_back.h6,game_back)
                        elif game_back.build[i][j][0]=='c' :
                            if game_back.build[i][j][1]=='1' :
                                return self.hitlol(game_back.c1,game_back)
                            elif game_back.build[i][j][1]=='2' :
                                return self.hitlol(game_back.c2,game_back)
                            elif game_back.build[i][j][1]=='3' :
                                return self.hitlol(game_back.c3,game_back)
                            elif game_back.build[i][j][1]=='4' :
                                return self.hitlol(game_back.c4,game_back)
                    elif game_back.build[i][j]=='t' :
                        game_back.t.changehealth(game_back,self.damageTH)
                        if game_back.t.health<=0 :
                            game_back.t.remove_TH(game_back)
                            game_back.no_of_buildings-=1
                            if(game_back.no_of_buildings<=0):
                                return game_back.game_over(1)
                        return 0

    def move(self,game_back):
        # print(self.health)
        # print("\033[1;1"+str(self.health))
        print("\033[1;1H"+self.health)
        if(self.health>0):    
            mi=200
            m=[0,0]
            no=0
            p=[[7,33,game_back.h1.health],[17,33,game_back.h2.health],[27,33,game_back.h3.health],[7,99,game_back.h4.health],[17,99,game_back.h5.health],[27,99,game_back.h6.health],[15,65,game_back.t.health],[11,44,game_back.c1.health],[23,44,game_back.c2.health],[11,88,game_back.c3.health],[23,88,game_back.c4.health]]
            for i in range(0,len(p)):
                if(p[i][2]>0):
                    if abs(abs(p[i][0]-self.x)+abs(p[i][1]-self.y))<mi:
                        mi=abs(abs(p[i][0]-self.x)+abs(p[i][1]-self.y))
                        m=list(p[i][0:2])
                        no=i
            x=self.x
            y=self.y
            if no==6:
                i=14
                j=63
                p=5
                q=3
            else:
                i=m[0]-2
                j=m[1]-2
                p=1
                q=1
            if no>6:
                self.changehealth(game_back,50)
            if x<=i and y<=j:
                if(game_back._grid[x+1][y+1]=='\033[31m'+' '+'\033[0m'):
                    game_back.build[self.x][self.y]='n'
                    game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                    self.x+=1
                    self.y+=1
                    game_back.build[self.x][self.y]='b'
                    game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                    #sleep(0.05)
                if(game_back._grid[x+1][y+1]=='\x1b[33m■\x1b[0m'):
                    game_back.build[x+1][y+1]='n'
                    game_back.change_grid(x+1,y+1,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(x+2)+";"+str(y+2)+"H"+'\033[31m'+' '+'\033[0m')
                    #sleep(0.05)
            elif x<=i and y>=j+p:
                if(game_back._grid[x+1][y-1]=='\033[31m'+' '+'\033[0m'):
                    game_back.build[self.x][self.y]='n'
                    game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                    self.x+=1
                    self.y-=1
                    game_back.build[self.x][self.y]='b'
                    game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                    #sleep(0.05)
                if(game_back._grid[x+1][y-1]=='\x1b[33m■\x1b[0m'):
                    game_back.build[x+1][y-1]='n'
                    game_back.change_grid(x+1,y-1,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(x+2)+";"+str(y)+"H"+'\033[31m'+' '+'\033[0m')
                    #sleep(0.05)
            elif x>=i+q and y<=j:
                if(game_back._grid[x-1][y+1]=='\033[31m'+' '+'\033[0m'):
                    game_back.build[self.x][self.y]='n'
                    game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                    self.x-=1
                    self.y+=1
                    game_back.build[self.x][self.y]='b'
                    game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                    #sleep(0.05)
                if(game_back._grid[x-1][y+1]=='\x1b[33m■\x1b[0m'):
                    game_back.build[x-1][y+1]='n'
                    game_back.change_grid(x-1,y+1,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(x)+";"+str(y+2)+"H"+'\033[31m'+' '+'\033[0m')
                    #sleep(0.05)
            elif x>=i+q and y>=j+p:
                if(game_back._grid[x-1][y-1]=='\033[31m'+' '+'\033[0m'):
                    game_back.build[self.x][self.y]='n'
                    game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                    self.x-=1
                    self.y-=1
                    game_back.build[self.x][self.y]='b'
                    game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                    print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                    #sleep(0.05)
                if(game_back._grid[x-1][y-1]=='\x1b[33m■\x1b[0m'):
                    game_back.build[x-1][y-1]='n'
                    game_back.change_grid(x-1,y-1,'\033[31m'+' '+'\033[0m')
                    print("\033["+str(x)+";"+str(y)+"H"+'\033[31m'+' '+'\033[0m')
                    #sleep(0.05)
            elif no==6:
                if(x==15 and y<j) or (y==64 or 65 and x<i):
                    if(game_back._grid[x+1][y+1]=='\x1b[33m■\x1b[0m'):
                        game_back.build[x+1][y+1]='n'
                        game_back.change_grid(x+1,y+1,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(x+2)+";"+str(y+2)+"H"+'\033[31m'+' '+'\033[0m')
                        #sleep(0.05)
                    if(game_back._grid[x+1][y+1]=='\033[31m'+' '+'\033[0m'):
                        game_back.build[self.x][self.y]='n'
                        game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                        self.x+=1
                        self.y+=1
                        game_back.build[self.x][self.y]='b'
                        game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')    
                elif(x==15 and y>j) or (y==67 or 66 and x<i):
                    if(game_back._grid[x+1][y-1]=='\x1b[33m■\x1b[0m'):
                        game_back.build[x+1][y-1]='n'
                        game_back.change_grid(x+1,y-1,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(x+2)+";"+str(y)+"H"+'\033[31m'+' '+'\033[0m')
                        #sleep(0.05)
                    if(game_back._grid[x+1][y-1]=='\033[31m'+' '+'\033[0m'):
                        game_back.build[self.x][self.y]='n'
                        game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                        self.x+=1
                        self.y-=1
                        game_back.build[self.x][self.y]='b'
                        game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                elif(x==16 and y<j) or (y==64 or 65 and x>i+q):
                    if(game_back._grid[x-1][y+1]=='\x1b[33m■\x1b[0m'):
                        game_back.build[x-1][y+1]='n'
                        game_back.change_grid(x-1,y+1,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(x)+";"+str(y+2)+"H"+'\033[31m'+' '+'\033[0m')
                        #sleep(0.05)
                    if(game_back._grid[x-1][y+1]=='\033[31m'+' '+'\033[0m'):
                        game_back.build[self.x][self.y]='n'
                        game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                        self.x-=1
                        self.y+=1
                        game_back.build[self.x][self.y]='b'
                        game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
                elif(x==16 and y>j) or (y==67 or 66 and x>i+q):
                    if(game_back._grid[x-1][y-1]=='\x1b[33m■\x1b[0m'):
                        game_back.build[x-1][y-1]='n'
                        game_back.change_grid(x-1,y-1,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(x)+";"+str(y)+"H"+'\033[31m'+' '+'\033[0m')
                        #sleep(0.05)
                    if(game_back._grid[x-1][y-1]=='\033[31m'+' '+'\033[0m'):
                        game_back.build[self.x][self.y]='n'
                        game_back.change_grid(self.x,self.y,'\033[31m'+' '+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+'\033[31m'+' '+'\033[0m')
                        self.x-=1
                        self.y-=1
                        game_back.build[self.x][self.y]='b'
                        game_back.change_grid(self.x,self.y,'\033[31m'+'B'+'\033[0m')
                        print("\033["+str(self.x+1)+";"+str(self.y+1)+"H"+"B"+'\033[0m')
            return self.hit(game_back)

    def changehealth(self,game_back,damage):
        # sleep(0.05)
        if self.health>0 :
            self.health-=damage
            if self.health<=0 :
                game_back.no_of_troops-=1
                self.remove(game_back)
    
class Spell():
    def __init__(self,name,game_back,king,barbarians):
        self.name=name
        if(name=="Fire"):
            king.movement*=2
            king.damageTH*=2
            king.damageall*=2
            for i in range(len(barbarians)):
                barbarians[i].damageall*=2
                barbarians[i].damageTH*=2
        elif(name=="Health"):
            king.health*=1.5
            for i in range(len(barbarians)):
                barbarians[i].health*=1.5
                if(barbarians[i].health>100):
                    barbarians[i].health=100
            if(king.health>100):
                king.health=100
            game_back.health=king.health
            
