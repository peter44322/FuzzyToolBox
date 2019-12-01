
import matplotlib.pyplot as plt


class Plotter:
    def variable(self, var):
        my_colors = plt.rcParams['axes.prop_cycle']()
        barColors = []
        for term in var.terms:
            color = next(my_colors)
            barColors.append(color)
            mf = term.membershipFunction
            plt.plot((0, 0), (0, 0), **color, label=term.name)
            for line in mf.lines:
                if term.name in var.fuzzyValue:
                    plt.plot(
                        line.xs(), (var.fuzzyValue[term.name], var.fuzzyValue[term.name]), **color)
                plt.plot(line.xs(), line.ys(), **color)

        plt.title(var.name)
        plt.legend(loc=1)
        # plt.show()
        return plt

    def line(self, line):
        plt.plot(line.xs(), line.ys())
        plt.show()

    def polygon(self, points):
        pointss = points
        # pointss.append(points[0])
        xs, ys = zip(*pointss)
        plt.scatter(xs, ys)
        plt.show()

    def polygonWithVar(self, points, var):
        pointss = points
        pointss.append(points[0])
        xs, ys = zip(*pointss)
        plt = self.variable(var)
        plt.plot(xs, ys)
        plt.show()
