import math

def teilor(x, n):
    sum = 0
    for i in range(n):
        sum += (x ** (2 * n + 1))/(2 * n + 1)
    return sum

def table_tailor(x, x0, dx, n):
    print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format("+","-"*10, "+", "-"*10, '+'))
    print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format('|', 'x', "|",'y','|'))
    print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format("+","-"*10, "+", "-"*10, '+'))
    while x0 < x:
        print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format("+","-"*10, "+", "-"*10, '+'))
        print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format('|', round(x0, 8), "|", round(teilor(x0, n), 8), '|'))
        print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format("+","-"*10, "+", "-"*10, '+'))
        x0 += dx



x0 = float(input("Введите x из диапозона от -1 до 1, x0="))
x = float(input("Введите x из диапозона от -1 до 1, x > x0, x="))
dx = float(input("Введите шаг приращения, dx="))
n = int(input("Введите число шагов для ряда Тейлора, n="))
table_tailor(x, x0, dx, n)
