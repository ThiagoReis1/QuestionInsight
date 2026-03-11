from numpy import*
from math import*
p = eval(input("um numero real:"))
x = array(eval(input("vetor x:")))
y = array(eval(input("vetor y:")))
q = p/(p-1)
r = 0
for i in range(size(x)):
	r = r + abs(x[i] + y[i])**q
s = r**(1/q)
print(round(s,5))