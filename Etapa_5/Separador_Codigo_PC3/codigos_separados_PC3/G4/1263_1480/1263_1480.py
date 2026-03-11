from numpy import *
from math import *

p = float(input("p: "))
x = array(eval(input("x: ")))
y = array(eval(input("y: ")))
t = (p)/(p+1)
x = 2 * x
y = 3 * y
norma = 0
for i in range(size(x)):
	norma = ((abs(x[i] + y[i]))**t)+norma
norma = norma ** (1/t)
print(round(norma,7))