import numpy as np
import math

class Point2D(object):
    #класс точка в двумерном пространстве с координатами x,y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_p(self,st='point'):
        # Метод - печатает строку плюс координаты точки
        # если p = Point2D(0,1), то p.print_p('Hello, Point') напечатает 'Hello, Point' 0 1
        print(st, self.x, self.y)

    def point_to_point(self, p2):
        # вычисляет угол между двумя векторами, проведенными из начала координат в точку (self) и точку р2
        r_self = (self.x * self.x + self.y * self.y) ** 0.5
        r_p2 = (p2.x * p2.x + p2.y * p2.y) ** 0.5
        if r_self == 0 or r_p2 == 0:
            return 0.
        try:
            cos_self_p2 = (self.x / r_self * p2.x / r_p2 + self.y / r_self * p2.y / r_p2)
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!')
            cos_self_p2 = 0
        sin_self_p2 = (1 - cos_self_p2 * cos_self_p2) ** 0.5
        try:
            fi = math.acos(cos_self_p2)
        except:
            fi = 0

        return -abs(fi)

    def new_pn(self,pc,fi):
        # Построение матрицы вращения точки вокруг начала координат, fi - угол поворота

        tr = [[math.cos(fi), -math.sin(fi)], [math.sin(fi), math.cos(fi)]]
        r = np.dot(np.array([self.x, self.y]), tr)
        return  Point2D(r[0],r[1])

    def rotate(self, origin,fi):
        # Вычисление новой точки при вращении исходной точки вокруг точки origin. fi - угол поворота
        # например если точка p = Point2D(1,1), то результатом работы метода
        # b = p.rotate(pn.Point2D(2,2),math.pi/2) будет точка b = Point2D(3.0, 0.9999999999)
        ox = origin.x
        oy = origin.y

        cos = math.cos(fi)
        sin = math.sin(fi)
        qx = ox + cos* (self.x - ox) - sin * (self.y - oy)
        qy = oy + sin * (self.x - ox) + cos * (self.y - oy)
        return Point2D(qx, qy)
