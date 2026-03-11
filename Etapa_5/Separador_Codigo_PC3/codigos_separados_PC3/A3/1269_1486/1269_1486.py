from numpy import *
from math import *

p = float(input(""))
x = array(eval("")) 
y = array(eval(""))

t = p/(p + 1)

normaX = 0
normaY = 0
resultado = 0

for i in range(0, size(x)):
	normaX = normaX + abs(x[1] ** t)
	normaY = normaY + abs(y[1] ** t)

normaX = normaX ** (1/t)
normaY = normaY ** (1/t)
resultado = abs((normaX + normaY) + (normaX - normaY))
print(round(resultado, 7))