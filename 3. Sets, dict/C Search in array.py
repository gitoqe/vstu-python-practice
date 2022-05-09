'''
Реализуйте эффективный поиск элемента в массиве.

Входные данные
В первой строке входных данных содержатся натуральные числа N и K (1 ≤ N, K ≤ 100000).

Во второй строке записаны N целых чисел – элементы входного массива.

В третьей строке записаны K целых чисел – элементы, которые нужно поискать.

Все числа являются целыми и по модулю не превосходят 109.

Выходные данные
Для каждого искомого числа выведите его позицию во входном массиве (нумерация идёт с единицы).
Если число встречается несколько раз, то выведите самое левое вхождение.
Если число в массиве отсутствует, то выведите 0.
'''

N, K = list(map(int, '5 3'.split()))
num_elems = list(map(int, '2 4 5 5 2'.split()))
num_f = list(map(int, '2 5 9'.split()))

print(N, K)
print(num_elems)
print(num_f)


dickt = {}
for i, el in enumerate(num_elems):
    if el not in dickt:
        dickt[el] = i
print(dickt)

for el in num_f:
    if el in dickt:
        print(dickt[el] + 1, end=' ')
    else:
        print(0, end=' ')

# N, K = list(map(int, input().split()))
# num_elems = input().split()
# num_f = input().split()
#
# positions = {}
# for el in num_f:
#     positions[el] = 0
#
# for i, el in enumerate(num_elems):
#     if el in positions and positions[el] == 0:
#         positions[el] = i + 1
#
# for el in positions:
#     print(positions[el], end=' ')


# N, K = list(map(int, '5 0'.split()))
# num_elems = list(map(int, '2 4 5 5 2'.split()))
# num_f = list(map(int, '2 5 9 9'.split()))
#
# print(N, K)
# print(num_elems)
# print(num_f)
#
# positions = []
# for i in range(K):
#     positions.append(0)
# print(positions)
#
# print()
#
# for i in range(N):
#     print('el:', num_elems[i], 'i:', i)
#     for j in range(K):
#         print('sub', num_f[j], 'j:', j)
#         if num_elems[i] == num_f[j] and positions[j] == 0:
#             positions[j] = i + 1
#     print()
# print(positions)
#
# print('\nANSWER:')
# for el in positions:
#     print(el, end=' ')


# N, K = list(map(int, '5 0'.split()))
# num_elems = list(map(int, '2 4 5 5 2'.split()))
# num_f = list(map(int, '2 5 9 9 3'.split()))
#
# print(N, K)
# print(num_elems)
# print(num_f)
#
# positions = {}
# for el in num_f:
#     positions[el] = 0
# print(positions)
#
# print()
#
# for i, el in enumerate(num_elems):
#     print(el)
#     if el in positions and positions[el] == 0:
#         print('got ONE')
#         positions[el] = i + 1
#     print()
# print(positions)
#
# print('\nANSWER:')
# for el in positions:
#     print(positions[el], end=' ')
