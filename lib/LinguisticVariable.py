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
