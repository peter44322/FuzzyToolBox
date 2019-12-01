
from lib.FuzzySet import FuzzySet
from lib.LinguisticVariable import LinguisticVariable
from lib.LinguisticTerm import LinguisticTerm
from lib.Plotter import Plotter
from lib.rules.Rule import Rule


openingPrice = LinguisticVariable(name="openingPrice", terms=[
    LinguisticTerm('low', FuzzySet(0, 0, 50)),
    LinguisticTerm('medium', FuzzySet(0, 50, 100)),
    LinguisticTerm('high', FuzzySet(50, 100, 100)),
])
openingPrice.setCrispValue(30)


previousDayPrice = LinguisticVariable(name="previousDayPrice", terms=[
    LinguisticTerm('low', FuzzySet(0, 0, 50)),
    LinguisticTerm('medium', FuzzySet(0, 50, 100)),
    LinguisticTerm('high', FuzzySet(50, 100, 100)),
])
previousDayPrice.setCrispValue(80)

closingPrice = LinguisticVariable(name="closingPrice", terms=[
    LinguisticTerm('verylow', FuzzySet(0, 0, 25)),
    LinguisticTerm('low', FuzzySet(0, 25, 50)),
    LinguisticTerm('medium', FuzzySet(25, 50, 75)),
    LinguisticTerm('high', FuzzySet(50, 75, 100)),
    LinguisticTerm('veryhigh', FuzzySet(75, 100, 100)),
])


varList = [openingPrice, previousDayPrice, closingPrice]

rules = [
    "openingPrice = low AND previousDayPrice = medium then closingPrice = low",
    "openingPrice = medium AND previousDayPrice = medium then closingPrice = medium",
    "openingPrice = medium AND previousDayPrice = high then closingPrice = high",
]

for rule in rules:
    ruleObject = Rule()
    ruleObject.parse(rule, varList)
    ruleObject.evaluate()


plotter = Plotter()


print(closingPrice.fuzzyValue)
print(closingPrice.aggregate())


plotter.polygonWithVar(closingPrice.aggregate(), closingPrice)


plotter.variable(openingPrice)
plotter.variable(previousDayPrice)
plotter.variable(closingPrice)
