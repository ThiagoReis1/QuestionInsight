from numpy import*
from math import*
p = float(input())
x = array(eval(input()))
y = array(eval(input()))
q = p/(p+1)
norma = 0
soma = 0
for i in range(size(x)):
	soma = soma + (x[i] + y[i])**q
	
norma = abs(soma)**(1/q)
print(round(norma,3))