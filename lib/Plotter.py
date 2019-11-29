
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
                plt.plot(line.xs(), line.ys(), **color)

        plt.title(var.name)
        plt.legend(loc=1)

        plt.show()
