from numpy import*
from math import*


p = float(input("digite o p: "))
x = array(eval(input("digite o x: ")))
y = array(eval(input("digite o y: ")))
z= 2 * x - y
i = 0
t = p/(p-1)
for i in range(size(x)):
	if (p > 1):
		N = sqrt(abs(z[i])**(1/t))
print(round(N,5))	





