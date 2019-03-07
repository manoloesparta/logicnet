from math import exp

class MathFormulas:

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + exp(-x))

    @staticmethod
    def sigmoid_derivative(x):
       return MathFormulas.sigmoid(x) * (1 - MathFormulas.sigmoid(x))
