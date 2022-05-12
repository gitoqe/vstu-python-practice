from sys import stdin

'''
Реализуйте класс Matrix. Он должен содержать:

Конструктор от списка списков.
Гарантируется, что списки состоят из чисел, не пусты и все имеют одинаковый размер.
Конструктор должен копировать содержимое списка списков,
т. е. при изменении списков, от которых была сконструирована матрица, содержимое матрицы изменяться не должно.

Метод __str__, переводящий матрицу в строку.
При этом элементы внутри одной строки должны быть разделены знаками табуляции, а строки — переносами строк.
После каждой строки не должно быть символа табуляции и в конце не должно быть переноса строки.

Метод size без аргументов, возвращающий кортеж вида (число строк, число столбцов).
Пример теста с участием этого метода есть в следующей задаче этой недели.
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Matrix:
    def __init__(self, lists):
        #print('\n__init__:', lists)
        self.num_of_rows = len(lists)
        #print('rows:', self.num_of_rows)
        self.num_of_cols = len(lists[0])
        #print('cols:', self.num_of_cols)
        self.rows = []
        for lst in lists:
            self.rows.append(lst)

    def __str__(self):
        #print('__str__')
        result = ''
        for i, row in enumerate(self.rows):
            for j, el in enumerate(row):
                result += str(el)
                if j != self.num_of_cols - 1:
                    result += '\t'
            if i != self.num_of_rows - 1:
                result += '\n'
        return result

    def size(self):
        result = (self.num_of_rows, self.num_of_cols)
        return result

print('Test1:')
# Task 1 check 1
m = Matrix([[1, 0], [0, 1]])
print(bcolors.WARNING, m, bcolors.ENDC)
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(bcolors.WARNING, m, bcolors.ENDC)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(bcolors.WARNING, m, bcolors.ENDC)
# 1	0
# 0	1
# 2	0	0
# 0	1	10000
# -10	20	50	2443
# -5235	12	4324	4234


print('\nTest2:')
# Task 1 check 2
m1 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
m2 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
print(bcolors.WARNING, str(m1) == str(m2), bcolors.ENDC)
# True
print(m1)


print('\nTest3:')
# Task 1 check 3
m = Matrix([[1, 1, 1], [0, 100, 10]])
print(bcolors.WARNING, str(m) == '1\t1\t1\n0\t100\t10', bcolors.ENDC)
# True

print(m)
print('1\t1\t1\n0\t100\t10')

#exec(stdin.read())
