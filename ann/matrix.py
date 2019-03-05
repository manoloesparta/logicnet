from random import random


class Matrix:

    def __init__(self, rows, columns):
        self.shape = (rows, columns)
        self.rows = rows
        self.columns = columns
        self.matrix = [[random() for _ in range(rows)] for _ in range(columns)]

    def __repr__(self):
       print(self.matrix)

    @staticmethod
    def Mult(matrix1, matrix2):
        pass
