
from lib.FuzzySet import FuzzySet
from lib.LinguisticVariable import LinguisticVariable
from lib.LinguisticTerm import LinguisticTerm
from lib.Plotter import Plotter
from lib.rules.Rule import Rule


position = LinguisticVariable(name="position", terms=[
    LinguisticTerm('Left', FuzzySet(0, 0, 10, 35)),
    LinguisticTerm('LeftCenter', FuzzySet(30, 40, 50)),
])
position.setCrispValue(10)

angel = LinguisticVariable(name="angel", terms=[
    LinguisticTerm('RBelow', FuzzySet(-90, -45, 9)),
    LinguisticTerm('RUpper', FuzzySet(-9, 23, 54)),
])
angel.setCrispValue(-45)


firePosition = LinguisticVariable(name="firePosition", terms=[
    LinguisticTerm('NegBig', FuzzySet(-30, -30, -15)),
    LinguisticTerm('NegMed', FuzzySet(-25, -15, -5)),
    LinguisticTerm('NegSm', FuzzySet(-12, -6, 0)),
])

varList = [position, angel, firePosition]

rule1 = Rule()
rule1.parse(
    "position = Left AND angel = RBelow then firePosition = NegBig", varList)


plotter = Plotter()

print(rule1.evaluate().fuzzyValue)


plotter.variable(position)
plotter.variable(angel)
plotter.variable(firePosition)
