'''
Дан целочисленный массив.
Найдите в нём элемент, который встречается чаще всего.
Если таких элементов несколько, то выведите наименьший из них.

Входные данные
В первой строке входных данных записано целое число N – размер массива (1 ≤ N ≤ 3·105).

Во второй строке записаны N целых чисел в диапазоне от 1 до 109 – элементы массива.

Выходные данные
Выведите одно целое число – ответ.
'''

N = int(input())
numbers = map(int, input().split())
stat = {}
for el in numbers:
    stat[el] = stat.get(el, 0) + 1
m_key = -1
m_count = -1
for key, count in stat.items():
    if m_count < count:
        m_key = key
        m_count = count
    elif m_count == count and key < m_key:
        m_key = key
        m_count = count
print(m_key)
