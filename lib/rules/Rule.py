from lib.rules.Predict import Predict
from lib.rules.OR import OR
from lib.rules.AND import AND
from lib.rules.Premise import Premise


import re


class Rule:
    def __init__(self, predict=None, consequent=None):
        self.predict = predict
        self.consequent = consequent

    def parse(self, string, variabls):
        inputs = []
        rightSide = string.lower().split("then")[0]
        leftSide = string.lower().split("then")[1]
        premisesOR = rightSide.lower().split("or")
        premisesAND = rightSide.lower().split("and")

        if len(premisesAND) > 1:
            self.predict = AND()
            premises = premisesAND
        else:
            self.predict = OR()
            premises = premisesOR

        for premise in premises:
            p = premise.split("=")
            var = next((x for x in variabls if x.name.lower()
                        == p[0].lower().strip()), None)
            inputs.append(Premise(var, p[1].lower().strip()))

        c = leftSide.split('=')

        var = next((x for x in variabls if x.name.lower()
                    == c[0].lower().strip()), None)
        # inputs.append(Premise(var, c[1].lower().strip()))

        self.consequent = Premise(var, c[1].lower().strip())
        self.predict.setInputs(inputs)

    def evaluate(self):
        self.consequent.var.setFuzzyValue(
            self.consequent.termName, self.predict.evaluate().fuzzeyValue())
        return self.consequent.var
