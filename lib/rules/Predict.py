class Predict:
    def __init__(self,  inputs=[]):
        self.setInputs(inputs)

    def setInputs(self, inputs):
        self.inputs = []
        for input in inputs:
            if type(input) is Predict:
                self.inputs.append(input.evaluate())
            else:
                self.inputs.append(input)
