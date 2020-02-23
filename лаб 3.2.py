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
if a > b and r < a and b < r:
    for i in range(10):
        x = float(input("Введите x="))
        y = float(input("Введите y="))
        if a > b and r < a and b < r:
            if task_2(a, b, r, x, y):
                print(i+1, "-ый выстрел, попавший в координатами (", x, ";", y, ") попал в мишень.")
            else:
                print(i+1, "-ый выстрел, попавший в координатами (", x, ";", y, ") не попал в мишень.")
