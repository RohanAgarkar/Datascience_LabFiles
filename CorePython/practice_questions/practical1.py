import math

a = 2
b = -5
c = 3

if a == 0:
    raise ZeroDivisionError()

x1 = ((-1*b)+math.sqrt(b-4*a*c))
x2 = ((-1*b)-math.sqrt(b-4*a*c))

print(x1/(2*a), x2/(2*a))