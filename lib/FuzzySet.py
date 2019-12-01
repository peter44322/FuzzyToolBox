from lib.Line import Line


class FuzzySet:
    def __init__(self, *args):
        self.set = args
        if self.isTriangular():
            self.lines = [
                Line((args[0], 0), (args[1], 1)),
                Line((args[1], 1), (args[2], 0)),
            ]
        else:
            self.lines = [
                Line((args[0], 0), (args[1], 1)),
                Line((args[1], 1), (args[2], 1)),
                Line((args[2], 1), (args[3], 0)),
            ]

    def isTriangular(self):
        return len(self.set) == 3

    def fuzzify(self, value):
        fuzzification = []
        for line in self.lines:
            fuzzification.append(line.getY(value))
        return max(fuzzification)
