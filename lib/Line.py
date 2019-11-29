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
