from numpy import*
from math import*

p = float(input("Digite p: "))
x = array(eval(input("Digite x: ")))
y = array(eval(input("Digite y: ")))

t = p/(p - 1)
raiz= 1/t
v = 0
for j in range(size(x)):
	v = v + abs(2*x[j] - y[j])**t
	r = (v** raiz)
	
print (round(r, 4))

