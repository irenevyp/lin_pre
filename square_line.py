import math

import matplotlib.pyplot as plt
import copy
import numpy as np
import os
import imageio
from scipy.optimize import fsolve
import class_square as sq
import class_point2d as pn
import class_line as l
from matplotlib.animation import ArtistAnimation


def new_rotation(s, dfiee):
    # this function calculates vertexes of one rotation and forms squares to represent rotation
    for i in range(1, 6):
        fi = i * dfiee
        s.append(sq.Square(a, b.rotate(a, fi), c.rotate(a, fi), d.rotate(a, fi)))
    return s


# base square vertexes
dx = 1/(2**0.5)
a = pn.Point2D(1, 1)
b = pn.Point2D(1-dx, 1+dx)
c = pn.Point2D(1, 1+2**0.5)
d = pn.Point2D(1+dx, 1+dx)

s = []  # array of squares

# number of squares during one rotation
jk = 5
dfiee = math.pi/2/jk  # angle of each subrotation

s.append(sq.Square(a, b, c, d))  # first square vertexes a,b,c,d
number_of_rotations = 8

#  with open('sq.text','w') as f_out:
#    f_out.write('new\n')
#  sq.Square(a,b,c,d).square_print_to_file('sq.text','w')

for k in range(1, number_of_rotations):

    s = new_rotation(s, dfiee)
    last_square_num = len(s)-1
    print(last_square_num)
    # new vertexes base to next rotation
    a = copy.deepcopy(s[last_square_num].pb)
    b = copy.deepcopy(s[last_square_num].pc)
    c = copy.deepcopy(s[last_square_num].pd)
    d = copy.deepcopy(s[last_square_num].pa)
    print(f'new cycle, rotation number {k}')


frames = []
fig, ax = plt.subplots()
fig.setsize = (7, 7)
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
gr = ax.grid()
ax.set_aspect('equal', 'box')

for i in range(len(s)-1):

    line, = ax.plot([-5, 5], [-5, 5], 'k')
    line1, = ax.plot([s[i].pa.x, s[i].pb.x], [s[i].pa.y, s[i].pb.y], 'r')
    line2, = ax.plot([s[i].pa.x, s[i].pd.x], [s[i].pa.y, s[i].pd.y], 'g')
    line3, = ax.plot([s[i].pc.x, s[i].pb.x], [s[i].pc.y, s[i].pb.y], 'b')
    line4, = ax.plot([s[i].pc.x, s[i].pd.x], [s[i].pc.y, s[i].pd.y], 'k')
#    line5, = ax.plot([1,-4],[-4,1],'k')
    interval = 210

    frames.append([line, line1, line2, line3, line4])
    s[i].square_print_to_file('sq_line.text', 'a')


animation = ArtistAnimation(
        fig,  # animatio figure
        frames,  # frames
        interval=150,  # delay between frames, ms
        blit=True,  # whether to use double buffering
        repeat=True)  # whether to loop the animation

plt.show()
