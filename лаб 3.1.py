import math

def line_for_table():
    print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format("+","-"*10, "+", "-"*10, '+'))
        
def header_table():
    line_for_table()
    print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format('|', 'x', "|",'y','|'))
    line_for_table()
    
def table(dx, r):
    x0 = -10.0
    x1 = 4.0
    header_table()
    while x0 < x1:
        z = round(x0, 8)
        y = round(task_1(x0, r), 6)
        print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format('|', z, '|', y, '|'))
        line_for_table()
        x0 += dx

def task_1(x, r):
    if x >= -10 and x <= -6:
        return math.sqrt((r ** 2) - (x + 8) ** 2) - 2
    elif x > -6 and x <= -4:
        return 2
    elif x > -4 and x <= 2:
        return -0.5 * x
    elif x > 2 and x < 4:
        return x - 3

dx = float(input("Введите шаг приращения, dx="))
r = float(input("Введите радиус закругления, r="))

table(dx, r)
