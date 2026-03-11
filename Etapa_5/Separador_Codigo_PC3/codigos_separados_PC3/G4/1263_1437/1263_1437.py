from numpy import *
from math import *

p = float(input())
x = array(eval(input()))
y = array(eval(input()))

if p > 1:
	t = p/(p+1)
	z = array(zeros(size(x)))
	soma = 0
	
	for i in range(size(x)):
		z[i] = 2*x[i] + 3*y[i]
	for i in range(size(z)):
		soma = soma + (abs(z[i]))**t
	raiz = soma**(1/t)
	print(round(raiz,7))
	
	
	