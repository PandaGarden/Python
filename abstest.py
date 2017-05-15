import math
def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def argvalidation(l,type):
    for x in l:
        if not isinstance(x,(type)):
            raise TypeError ('xxxxx')
        else:
            pass

def quadratic(a,b,c):
    delta = b*b - (4*a*c)
    nx = (-b+math.sqrt(delta))/(2*a)
    ny = (-b-math.sqrt(delta))/(2*a)
    return nx, ny

print (quadratic(2,3,1))
print (quadratic(1,3,-4))