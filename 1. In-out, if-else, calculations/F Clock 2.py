'''
С начала суток часовая стрелка повернулась на угол в α градусов.
Определите на какой угол повернулась минутная стрелка с начала последнего часа.
Входные и выходные данные — действительные числа.
'''

a = float(input())
answer = a / 360.0 * 12 % 1 * 360.0
print(answer)
