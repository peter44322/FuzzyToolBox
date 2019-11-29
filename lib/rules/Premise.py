class Premise:
    def __init__(self, var, termName):
        self.var = var
        self.termName = termName

    def fuzzeyValue(self):
        return self.var.fuzzyValueOf(self.termName)
