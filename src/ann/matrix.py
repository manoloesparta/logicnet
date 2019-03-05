from random import randint

class Matrix:

    def __init__(self, rows, columns):
        self.shape = (rows, columns)

        rows_temp = [0 for i in range(rows)]
        total = [rows_temp for i in range(columns)]
        self.matrix = total

    def randomize(self):
        pass