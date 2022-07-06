import imp
from .classes import *

def set_buildings(i,game_back,j):
    if j==1:
        if i==0:
            # game_back = board(rows,columns, frames)
            game_back.k = king()
            game_back.no_of_buildings=11
            game_back.t=TH()
            game_back.t.set_TH(game_back)
            game_back.c1,game_back.c2,game_back.c3,game_back.c4=cannon(),cannon(),cannon(),cannon()
            game_back.c1.k=1
            game_back.c2.k=2
            game_back.c3.k=3
            game_back.c4.k=4
            game_back.c2.set_cannon(23,44,game_back)
            game_back.c1.health=100
            game_back.c3.set_cannon(11,88,game_back)
            game_back.c3.health=100
            game_back.c1.set_cannon(11,44,game_back)
            game_back.c2.health=100
            game_back.c4.set_cannon(23,88,game_back)
            game_back.c4.health=100
            game_back.h1=hut()
            game_back.h1.k=1
            game_back.h2=hut()
            game_back.h2.k=2
            game_back.h3=hut()
            game_back.h3.k=3
            game_back.h4=hut()
            game_back.h4.k=4
            game_back.h5=hut()
            game_back.h5.k=5
            game_back.h6=hut()
            game_back.h6.k=6
            game_back.h1.set_hut(7,33,game_back)
            game_back.h4.set_hut(7,99,game_back)
            game_back.h3.set_hut(27,33,game_back)
            game_back.h6.set_hut(27,99,game_back)
            game_back.h2.set_hut(17,33,game_back)
            game_back.h5.set_hut(17,99,game_back)
            game_back.w=wall()
            game_back.w.set_wall(11,54,20,76,game_back)
            game_back.w.set_wall(3,25,28,103,game_back)
            game_back.set_spawning_points1x=13
            game_back.set_spawning_points1y=2
            game_back.set_spawning_points2x=1
            game_back.set_spawning_points2y=63
            game_back.set_spawning_points3x=13
            game_back.set_spawning_points3y=127
            game_back.set_spawning_point(game_back.set_spawning_points1x,game_back.set_spawning_points1y,game_back.set_spawning_points2x,game_back.set_spawning_points2y,game_back.set_spawning_points3x,game_back.set_spawning_points3y)
            game_back.show_grid()
        if i==1:
            game_back.show_grid()
    if j==2:
        if i==0:
                # game_back = board(rows,columns, frames)
            game_back.no_of_buildings=11
            game_back.t=TH()
            game_back.t.set_TH(game_back)
            game_back.c1,game_back.c2,game_back.c3,game_back.c4=cannon(),cannon(),cannon(),cannon()
            game_back.c1.k=1
            game_back.c2.k=2
            game_back.c3.k=3
            game_back.c4.k=4
            game_back.c2.set_cannon(23,44,game_back)
            game_back.c1.health=100
            game_back.c3.set_cannon(11,88,game_back)
            game_back.c3.health=100
            game_back.c1.set_cannon(11,44,game_back)
            game_back.c2.health=100
            game_back.c4.set_cannon(23,88,game_back)
            game_back.c4.health=100
            game_back.h1=hut()
            game_back.h1.k=1
            game_back.h2=hut()
            game_back.h2.k=2
            game_back.h3=hut()
            game_back.h3.k=3
            game_back.h4=hut()
            game_back.h4.k=4
            game_back.h5=hut()
            game_back.h5.k=5
            game_back.h6=hut()
            game_back.h6.k=6
            game_back.h1.set_hut(7,33,game_back)
            game_back.h4.set_hut(7,99,game_back)
            game_back.h3.set_hut(27,33,game_back)
            game_back.h6.set_hut(27,99,game_back)
            game_back.h2.set_hut(17,33,game_back)
            game_back.h5.set_hut(17,99,game_back)
            game_back.w=wall()
            game_back.w.set_wall(11,54,20,76,game_back)
            game_back.w.set_wall(3,25,28,103,game_back)
            game_back.set_spawning_points1x=13
            game_back.set_spawning_points1y=2
            game_back.set_spawning_points2x=1
            game_back.set_spawning_points2y=63
            game_back.set_spawning_points3x=13
            game_back.set_spawning_points3y=127
            game_back.set_spawning_point(game_back.set_spawning_points1x,game_back.set_spawning_points1y,game_back.set_spawning_points2x,game_back.set_spawning_points2y,game_back.set_spawning_points3x,game_back.set_spawning_points3y)
            game_back.show_grid()

        if i==1:
            game_back.show_grid()
    if j==3:
        if i==0:
                # game_back = board(rows,columns, frames)
            game_back.no_of_buildings=11
            game_back.t=TH()
            game_back.t.set_TH(game_back)
            game_back.c1,game_back.c2,game_back.c3,game_back.c4=cannon(),cannon(),cannon(),cannon()
            game_back.c1.k=1
            game_back.c2.k=2
            game_back.c3.k=3
            game_back.c4.k=4
            game_back.c2.set_cannon(23,44,game_back)
            game_back.c1.health=100
            game_back.c3.set_cannon(11,88,game_back)
            game_back.c3.health=100
            game_back.c1.set_cannon(11,44,game_back)
            game_back.c2.health=100
            game_back.c4.set_cannon(23,88,game_back)
            game_back.c4.health=100
            game_back.h1=hut()
            game_back.h1.k=1
            game_back.h2=hut()
            game_back.h2.k=2
            game_back.h3=hut()
            game_back.h3.k=3
            game_back.h4=hut()
            game_back.h4.k=4
            game_back.h5=hut()
            game_back.h5.k=5
            game_back.h6=hut()
            game_back.h6.k=6
            game_back.h1.set_hut(7,33,game_back)
            game_back.h4.set_hut(7,99,game_back)
            game_back.h3.set_hut(27,33,game_back)
            game_back.h6.set_hut(27,99,game_back)
            game_back.h2.set_hut(17,33,game_back)
            game_back.h5.set_hut(17,99,game_back)
            game_back.w=wall()
            game_back.w.set_wall(11,54,20,76,game_back)
            game_back.w.set_wall(3,25,28,103,game_back)
            game_back.set_spawning_points1x=13
            game_back.set_spawning_points1y=2
            game_back.set_spawning_points2x=1
            game_back.set_spawning_points2y=63
            game_back.set_spawning_points3x=13
            game_back.set_spawning_points3y=127
            game_back.set_spawning_point(game_back.set_spawning_points1x,game_back.set_spawning_points1y,game_back.set_spawning_points2x,game_back.set_spawning_points2y,game_back.set_spawning_points3x,game_back.set_spawning_points3y)
            game_back.show_grid()

        if i==1:
            game_back.show_grid()