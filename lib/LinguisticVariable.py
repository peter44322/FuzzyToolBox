from lib.Line import Line


class LinguisticVariable:
    def __init__(self, name, terms, varRange=[]):
        self.name = name
        self.varRange = varRange
        self.terms = terms
        self.crispValue = None
        self.fuzzyValue = {}

    def fuzzify(self):
        self.fuzzyValue = {}
        for term in self.terms:
            self.fuzzyValue[term.name.lower()] = term.membershipFunction.fuzzify(
                self.crispValue)
        return self.fuzzyValue

    def setCrispValue(self, value):
        self.crispValue = value
        self.fuzzify()

    def setFuzzyValue(self, term, value):
        self.fuzzyValue[term] = value

    def fuzzyValueOf(self, termName):
        return self.fuzzyValue[termName.lower()]

    def aggregate1(self):
        lines = []
        points = []
        yLimits = []
        xAxis = Line((0, 0), (1, 0))

        for term in self.terms:
            for line in [term.membershipFunction.lines[0], term.membershipFunction.lines[-1]]:
                lines.append(line)
                if term.name in self.fuzzyValue:
                    yLimits.append(self.fuzzyValue[term.name])
                else:
                    yLimits.append(0)
            if term.name in self.fuzzyValue:
                lines += [Line((0, self.fuzzyValue[term.name]),
                               (10, self.fuzzyValue[term.name]))]
                yLimits.append(self.fuzzyValue[term.name])

        # lines += [xAxis]
        # yLimits.append(1)
        print(len(yLimits), len(lines))
        for idx, line in enumerate(lines):
            for a in lines:
                point = line.intersectWith(a)
                if point != None and point[1] >= 0 and point[1] <= yLimits[idx] and point not in points:
                    points.append(point)

        return points

    def aggregate(self):
        lines = []
        points = []
        yLimits = []
        xAxis = Line((0, 0), (1, 0))
        lastLine = None
        lastUpper = None
        for term in self.terms:
            if term.name in self.fuzzyValue:
                y = self.fuzzyValue[term.name]
                firstLine = term.membershipFunction.lines[0]
                secondLine = term.membershipFunction.lines[-1]
                upperLine = Line(
                    (0, y), (10, y))
                points.append(firstLine.intersectWith(upperLine))
                points.append(secondLine.intersectWith(upperLine))
                points.append(firstLine.point1)
                points.append(secondLine.point2)
                if lastLine != None:
                    point = firstLine.intersectWith(lastLine)
                    if point != None and point[1] < y:
                        points.append(firstLine.intersectWith(lastLine))
                        points.append(firstLine.intersectWith(lastUpper))

                lastLine = secondLine
                lastUpper = upperLine

        return points

    def crispValue(self):
        pass
