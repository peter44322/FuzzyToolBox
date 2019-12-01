class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def getY(self, x):
        if self.slope() == None:
            if(x == self.point1[0]):
                return 1
            else:
                return 0

        y = (self.slope() * x) + self.yIntercept()
        if y >= 0 and y <= 1:
            return y
        else:
            return 0

    def slope(self):
        y2 = self.point2[1]
        y1 = self.point1[1]
        x2 = self.point2[0]
        x1 = self.point1[0]
        if(x2-x1) == 0:
            return None
        return (y2-y1)/(x2-x1)

    def yIntercept(self):
        y = self.point1[1]
        x = self.point1[0]
        return y - (self.slope() * x)

    def xs(self):
        x2 = self.point2[0]
        x1 = self.point1[0]
        return (x1, x2)

    def ys(self):
        y2 = self.point2[1]
        y1 = self.point1[1]
        return (y1, y2)

    def xDiff(self, otherLine):
        x11, x12 = self.xs()
        x21, x22 = otherLine.xs()
        return (x11 - x12, x21-x22)

    def yDiff(self, otherLine):
        y11, y12 = self.ys()
        y21, y22 = otherLine.ys()
        return (y11 - y12, y21-y22)

    def intersectWith(self, otherLine):
        xdiff = self.xDiff(otherLine)
        ydiff = self.yDiff(otherLine)

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            return None

        d = (det(self.point1, self.point2), det(
            otherLine.point1, otherLine.point2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y
