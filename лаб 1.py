import math

def z1(a):
    return (math.sin(math.pi/2 + 3 * a))/(1 - math.sin(3 * a - math.pi))
    
def z2(a):
    return ctg(1.25 * math.pi + 1.5 * a)

def ctg(a):
    return math.cos(a)/math.sin(a)
    
a = float(input("Введите значение a="))
print(z1(a), z2(a))
