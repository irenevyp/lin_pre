import matplotlib.pyplot as plt
import copy
import numpy as np
import os
import imageio


class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, pa, pb):
        self.pa = pa
        self.pb = pb

    def line_plt(self, col='r'):
        # plotting a line between two points
        ax.plot([self.pa.x, self.pb.x], [self.pa.y, self.pb.y], col = 'k')

    def line_div(self, n = 20):
        dx = (self.pb.x-self.pa.x)/n
        dy = (self.pb.y-self.pa.y)/n
        return [dx,dy]


class Square:

    def __init__(self, pa, pb, pc, pd):
        self.pa = pa
        self.pb = pb
        self.pc = pc
        self.pd = pd


    def square_plt(self, col = 'k'):
        # plotting quadrangle
        ax.plot([self.pa.x, self.pb.x], [self.pa.y, self.pb.y], col)
        ax.plot([self.pa.x, self.pd.x], [self.pa.y, self.pd.y], col)
        ax.plot([self.pc.x, self.pb.x], [self.pc.y, self.pb.y], col)
        ax.plot([self.pc.x, self.pd.x], [self.pc.y, self.pd.y], col)

    def square_transform(self, dd = [[0.1, 0.1], [0.1, 0.1], [0.2, 0.2], [0.2, 0.2]]):
        #transformation of a quadrangle
        self.pa.x = self.pa.x + dd[0][0]
        self.pa.y = self.pa.y + dd[0][1]
        self.pb.x = self.pb.x + dd[1][0]
        self.pb.y = self.pb.y + dd[1][1]
        self.pc.x = self.pc.x+dd[2][0]
        self.pc.y = self.pc.y + dd[2][1]
        self.pd.x = self.pd.x+dd[3][0]
        self.pd.y = self.pd.y + dd[3][1]

    def square_lin_transform(self, tr_matr=np.array([[-3, 0.5], [1.5, 3]])):
        # linear transformation of a quadrangle
        r = np.dot(np.array([self.pa.x, self.pa.y]),tr_matr)
        self.pa = Point2D(r[0],r[1])
        r = np.dot(np.array([self.pb.x, self.pb.y]),tr_matr)
        self.pb = Point2D(r[0], r[1])
        r = np.dot(np.array([self.pc.x, self.pc.y]), tr_matr)
        self.pc = Point2D(r[0], r[1])
        r = np.dot(np.array([self.pd.x, self.pd.y]), tr_matr)
        self.pd = Point2D(r[0], r[1])


# initial assignments of the four vertices of the quadrilateral
a = Point2D(-1, 1)
b = Point2D(-1, 2)
c = Point2D(2, 2)
d = Point2D(2, -1)
# number of transformation quadrangles
n = 100

# initial quadrangle
s = Square(a, b, c, d)


#new quadrangle - the result of linear transformation
s3 = copy.deepcopy(s)
s3.square_lin_transform()

# schedule boundaries
xmin = int(min(s.pa.x, s.pb.x, s.pc.x, s.pd.x, s3.pa.x, s3.pb.x, s3.pc.x, s3.pd.x))-1
ymin = int(min(s.pa.y, s.pb.y, s.pc.y, s.pd.y, s3.pa.y, s3.pb.y, s3.pc.y, s3.pd.y))-1
xmax = int(max(s.pa.x, s.pb.x, s.pc.x, s.pd.x, s3.pa.x, s3.pb.x, s3.pc.x, s3.pd.x))+1
ymax = int(max(s.pa.y, s.pb.y, s.pc.y, s.pd.y, s3.pa.y, s3.pb.y, s3.pc.y, s3.pd.y))+1
# lines connecting the vertices of the source and destination quadrilateral
# each vertex of the original quad will crawl along a straight line connecting this vertex to the resulting vertex
l_aa = Line(s.pa, s3.pa)
l_bb = Line(s.pb, s3.pb)
l_cc = Line(s.pc, s3.pc)
l_dd = Line(s.pd, s3.pd)
#dividing lines  n parts

d_aa = l_aa.line_div(n)
d_bb = l_bb.line_div(n)
d_cc = l_cc.line_div(n)
d_dd = l_dd.line_div(n)
# first transformation quadrangle
s_1 = copy.deepcopy(s)
s_1.square_transform([d_aa,d_bb, d_cc, d_dd])
# array of transformation quadrangles
s_t = []
s_t.append (s_1)
# array of filenames to make gif file
filenames = []
for i in range(n):
# matplotlib assignments
    fig, ax = plt.subplots()
    fig.setsize = (6, 6)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    gr = ax.grid()
    ax.set_aspect('equal', 'box')
#plotting original quadrangle in red color
    s.square_plt('r')
# new quadrangle
    s_1 = copy.deepcopy(s_1)
    s_1.square_transform([d_aa, d_bb, d_cc, d_dd])
    s_t.append(s_1)
#plotting next quadrangle in black color
    s_1.square_plt()
#plotting resulting quadrangle in green color
    s3.square_plt('g')

    title = ax.text(0.5, 1.05, "Трансформируюсь, шаг № {}".format(i),
                    size=plt.rcParams["axes.titlesize"],
                    ha="center", transform=ax.transAxes, )

    filename = f'{i}.png'
    filenames.append(filename)
# save frame
    plt.savefig(filename)
    plt.close()

# build gif
with imageio.get_writer('squ_.gif', mode='I',fps= 250) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

        # Remove files
for filename in set(filenames):
    os.remove(filename)


