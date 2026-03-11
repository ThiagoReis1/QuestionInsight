from numpy import*
from math import*

p = float(input("digite p: "))
x = array(eval(input("digite x: ")))
y = array(eval(input("digite y: ")))
z = 2 * x - y
i = 0
t = p/(p+1)

for i in range(size(i)):
	if(p > 1):
		N = sqrt(abs(z[i])**(1/t))
print(round(N, 4))

