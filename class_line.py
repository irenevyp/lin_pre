import class_point2d as pn
import matplotlib.pyplot as plt


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def line_plt(self, col='r'):
        # plotting a line between two points
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y])

    def line_div(self, n = 20):
        dx = (self.p2.x-self.p1.x)/n
        dy = (self.p2.y-self.p1.y)/n
        return [dx,dy]

    def line_perp(self,r=1):
        # calculating perpendicular m from pointa with length=r
        k = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        m = -1 / k
        dx = (r*r/(1+m*m))**0.5
        dy = -m*dx
        if dx/dy!=m:
            dx=-dx
#        if (self.p1.x + dx) * (self.p1.x + dx) > (self.p1.y + dy):
#            dy = -dy
#            if dx / dy != m:
#                 dx = -dx

        return pn.Point2D(self.p1.x + dx, self.p1.y + dy)

    def line_perp1(self, r=1):
# calculating perpendicular m from pointa with length=r
        k = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        m = -1 / k
        dx = (r * r / (1 + m * m)) ** 0.5
        dy = -m * dx
        if dx / dy != m:
            dx = -dx
            if (self.p1.x + dx) * (self.p1.x + dx) > (self.p1.y + dy):
                dy = -dy
                if dx / dy != m:
                    dx = -dx

        return pn.Point2D(self.p1.x + dx, self.p1.y + dy)