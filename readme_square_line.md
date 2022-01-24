File square_line
with the help of matplotlib. ArtistAnimation 
represents rotation of a square on line. 
first square has coordinates of a vertexes a,b,c,d.
Rotation is carried out around the top a.
Therefore after each full rotation we choose new a vertex.
Rotation repeats in a cycle.

**program needs import of 'outer' libraries:**

import math

from matplotlib.animation import ArtistAnimation

import matplotlib.pyplot as plt

import copy

**and somehow 'inner libraries'**

import class_square as sq

import class_point2d as pn

import class_line as l
