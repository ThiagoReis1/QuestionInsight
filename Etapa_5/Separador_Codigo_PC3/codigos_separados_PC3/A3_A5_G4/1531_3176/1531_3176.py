from math import factorial
from math import pi

a = eval(input('angulo:'))
x = int(input('numero:'))

cos = 1 - (x**2/factorial(2)) + (x**4/factorial(4)) - (x**6/factorial(6)) + (x**8/factorial(8))

print (cos)
