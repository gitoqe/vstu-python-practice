'''
Добавьте в предыдущий класс следующие методы:

__add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
__mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
__rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа.
Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.
Иллюстрация:

В следующем случае вызовется __mul__:
Matrix([[0, 1], [1, 0]) * 10.

В следующем случае вызовется __rmul__ (так как у int не определен __mul__ для матрицы справа):
10 * Matrix([[0, 1], [1, 0]).

Разумеется, данные методы не должны менять содержимое матрицы.
'''

from sys import stdin
from copy import deepcopy


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            result = []
            numbers = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    summa = other.matrix[i][j] + self.matrix[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.matrix[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * j for j in i] for i in self.matrix]
            return Matrix(result)

    __rmul__ = __mul__


exec(stdin.read())
