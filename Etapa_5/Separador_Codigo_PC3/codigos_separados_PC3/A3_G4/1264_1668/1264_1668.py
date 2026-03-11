from numpy import * 
from math import * 
p = float(input("Digite o valor: "))
x = array(eval(input("Digite o valor de x: ")))
y = array(eval(input("Digite o valor de y: ")))

h = 0
n = 0
j = 0 

t = (p) / (p + 1)
xy = (x - (2 * y))

for i in xy:
	n = n + (abs(i)) ** t
v = n ** (1 / t)
print(round(v, 8))