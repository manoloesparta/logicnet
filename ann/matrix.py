from random import random

class Matrix:

    def __init__(self, cols, rows, zeros=False):
        self.cols = cols
        self.rows = rows
        self.shape = (cols, rows)

        if zeros:
            self.matrix = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        else:
            self.matrix = [[random() for _ in range(self.rows)] for _ in range(self.cols)]

    def __repr__(self):
        raw = str(self.matrix).split('],')
        return ']\n'.join(raw)

    def __add__(self, matrix):
        assert self.shape == matrix.shape, 'Not compatible shapes'
        cols, rows = self.shape
        result = Matrix(rows, cols, zeros=True)

        for i in range(cols):
           for j in range(rows):
              result.matrix[i][j] = self.matrix[i][j] + matrix.matrix[i][j]

        return result

    def T(self):
        rows, cols = self.shape
        result = Matrix(cols, rows, zeros=True)

        for i in range(cols):
            for j in range(rows):
                result.matrix[i][j] = self.matrix[j][i]

        self.shape = result.shape
        self.cols, self.rows = result.cols, result.rows
        self.matrix = result.matrix


    @staticmethod
    def matmul(matrix1, matrix2):
        assert matrix1.shape[1] == matrix2.shape[0], 'Not compatible shapes'
        result = Matrix(matrix1.shape[1], matrix2.shape[0], zeros=True)
        return result

