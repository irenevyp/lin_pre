import numpy as np
import matplotlib.pyplot as plt
class Square:
    # класс квадрат, но может также быть и четырехугольник
    def __init__(self, pa, pb, pc, pd):
        self.pa = pa
        self.pb = pb
        self.pc = pc
        self.pd = pd


    def square_plt(self, col = 'k'):
        # plotting quadrangle
        plt.plot([self.pa.x, self.pb.x], [self.pa.y, self.pb.y], col)
        plt.plot([self.pa.x, self.pd.x], [self.pa.y, self.pd.y], col)
        plt.plot([self.pc.x, self.pb.x], [self.pc.y, self.pb.y], col)
        plt.plot([self.pc.x, self.pd.x], [self.pc.y, self.pd.y], col)

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

    def square_print(self):
        # printing the vertexes of a quadrangle
        print('A=', self.pa.x, self.pa.y)
        print('B=', self.pb.x, self.pb.y)
        print('C=', self.pc.x, self.pc.y)
        print('D=', self.pd.x, self.pd.y)

    def square_print_to_file(self,file_name,reg):
        with open(file_name,'a') as f_out:

        # saving the vertexes of a quadrangle
            f_out.write('A= '+ str(self.pa.x)+' '+ str(self.pa.y)+';')
            f_out.write('B= '+ str(self.pb.x)+' '+ str(self.pb.y)+';')
            f_out.write('C= '+ str(self.pc.x)+' '+ str(self.pc.y)+';')
            f_out.write('D= '+ str(self.pd.x)+' '+ str(self.pd.y)+'\n')