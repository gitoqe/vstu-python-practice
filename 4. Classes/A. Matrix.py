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


class Matrix:
    def __init__(self, lists):
        print('\n__init__:', lists)
        print('№ of lists:', len(lists))
        self.rows = []
        for lst in lists:
            #print(lst)
            self.rows.append(lst)
        #print('list size:', len(self.rows[0]))
        print(lst)

    def __str__(self):
        print('__str__')
        result = ''
        for i, row in enumerate(self.rows):
            for j, el in enumerate(row):
                result += str(el)
                if j != len(row):
                    result += '\t'
            if i - 1 != len(self.rows):
                result += '\n'
        return result

    def size(self):
        return ()

print('Test1:')
# Task 1 check 1
m = Matrix([[1, 0], [0, 1]])
print(m)
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)
# 1	0
# 0	1
# 2	0	0
# 0	1	10000
# -10	20	50	2443
# -5235	12	4324	4234


print('\n\nTest2:')
# Task 1 check 2
m1 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
m2 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
print(str(m1) == str(m2))
# True
print(m1)


print('\n\nTest3:')
# Task 1 check 3
m = Matrix([[1, 1, 1], [0, 100, 10]])
print(str(m) == '1\t1\t1\n0\t100\t10')
# True

print(m)
print('1\t1\t1\n0\t100\t10')

#exec(stdin.read())
