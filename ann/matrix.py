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

    def __add__(self, addition):
        cols, rows = self.shape
        result = Matrix(cols, rows, zeros=True)

        for i in range(cols):
          for j in range(rows):
            result.matrix[i][j] = self.matrix[i][j] + addition

        return result

    def mat_add(self, addition):
        cols, rows = self.shape
        result = Matrix(cols, rows, zeros=True)

        assert self.shape == addition.shape, 'Not compatible shapes'

        for i in range(cols):
           for j in range(rows):
              result.matrix[i][j] = self.matrix[i][j] + addition.matrix[i][j]

        return result

    def __sub__(self, subtraction):
        cols, rows = self.shape
        result = Matrix(cols, rows, zeros=True)

        for i in range(cols):
            for j in range(rows):
                result.matrix[i][j] = self.matrix[i][j] - subtraction

        return result

    def mat_sub(self, subtraction):
        cols, rows = self.shape
        result = Matrix(cols, rows, zeros=True)

        assert self.shape == subtraction.shape, 'Not compatible shapes'

        for i in range(cols):
            for j in range(rows):
                result.matrix[i][j] = self.matrix[i][j] - subtraction.matrix[i][j]

        return result

    def __mul__(self, coef):
        cols, rows = self.shape
        result = Matrix(cols, rows, zeros=True)

        for i in range(cols):
            for j in range(rows):
                result.matrix[i][j] = self.matrix[i][j] * coef

        return result


    def mat_mul(self, matrix1, matrix2):
        assert matrix1.shape[1] == matrix2.shape[0], 'Not compatible shapes'
        result = Matrix(matrix1.shape[1], matrix2.shape[0], zeros=True)
        return result

    def T(self):
        rows, cols = self.shape
        result = Matrix(cols, rows, zeros=True)

        for i in range(cols):
            for j in range(rows):
                result.matrix[i][j] = self.matrix[j][i]

        return result

    def apply(self, func):
        cols, rows = self.shape
        result = Matrix(cols, rows, zeros=True)

        for i in range(cols):
            for j in range(rows):
               result.matrix[i][j] = func(self.matrix[i][j])

        return result

