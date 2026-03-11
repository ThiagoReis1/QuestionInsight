from numpy import *
from numpy import *

p = float(input(" Valores de p: "))
x = array(eval(input("valores de x: ")))
y = array(eval(input("valores de y: ")))
h = 0
n = 0
j = 0
t = ((p) / (p + 1))
xy = (1 * x + 1 * y)
for i in xy:
	n = n + (abs(i)) ** t
v = n ** (1 / t)
print(round(v , 3))