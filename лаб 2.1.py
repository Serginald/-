import math

def task_1(x, r):
    if x > -10 and x <= -6:
        return math.sqrt((r ** 2) - (x + 8) ** 2) - 2
    elif x > -6 and x <= -4:
        return 2
    elif x > -4 and x <= 2:
        return -0.5 * x
    elif x > 2 and x < 4:
        return x - 3
    else:
        return("Значение в не диапозоне.")
        
x = float(input("Введите x="))
r = float(input("Введите r="))

print("Значение функции:", task_1(x,r))
