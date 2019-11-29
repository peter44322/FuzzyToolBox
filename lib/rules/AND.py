from lib.rules.Predict import Predict
import operator


class AND(Predict):
    def evaluate(self):
        return min(self.inputs, key=lambda x: x.fuzzeyValue())
