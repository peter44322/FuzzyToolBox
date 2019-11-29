from lib.rules.Predict import Predict
import operator


class OR(Predict):
    def evaluate(self):
        return max(self.inputs,  key=lambda x: x.fuzzeyValue())
