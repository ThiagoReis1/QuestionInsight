from numpy import*
from math import*
p = float(input())
q = p/(p+1)
x = array(eval(input()))
y = array(eval(input()))
mod = 0
for i in range(0, size(x)):
	mod = mod + (abs(x[i] + y[i]))**q
res = (mod)**(1/q)
print(round(res,4))
	