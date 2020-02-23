import math

def task_2(a, b, r, x, y):
    if y < 0 and y > -b and -(math.sqrt(r ** 2 - x ** 2)) < y:
        return True
    elif y > 0 and y < b and math.sqrt(r ** 2 - y ** 2) < x and x < a:
        return True
    else:
        return False

a = float(input("Введите a="))
b = float(input("Введите b="))
r = float(input("Введите r="))
x = float(input("Введите x="))
y = float(input("Введите y="))

if a > b and r < a and b < r:
    if task_2(a, b, r, x, y):
        print("Точка с координатами (", x, ";", y, ") попала в закрашенную область.")
    else:
        print("Точка с координатами (", x, ";", y, ") не попала в закрашенную область.")
