from random import random


class Matrix:

    def __init__(self, rows, columns, zeros=False):
        self.shape = (rows, columns)
        self.rows = rows
        self.columns = columns

        if zeros:
            self.matrix = [[0 for _ in range(self.rows)] for _ in range(self.columns)]
        else:
            self.matrix = [[random() for _ in range(rows)] for _ in range(columns)]

    def __repr__(self):
        raw = str(self.matrix).split('],')
        return ']\n'.join(raw)

    @staticmethod
    def matmul(matrix1, matrix2):
        assert matrix1.shape[1] == matrix2.shape[0], 'Not compatible shapes'
        result = Matrix(matrix1.shape[1], matrix2.shape[0], zeros=True)
        return result

