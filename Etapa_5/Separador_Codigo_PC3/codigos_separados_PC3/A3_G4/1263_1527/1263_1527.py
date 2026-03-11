#ufam - Laís Amorim Reis - 21602327
from numpy import *
from math import *

p = float(input())

x = array(eval(input()))
y = array(eval(input()))
z = array(zeros(size(x),dtype = float))

for i  in range(0,size(x)):
	z[i] = (2*x[i])+(3*y[i]) 
t = p/(p+1)

norma = 0
result = 0

for i in range(0,size(z)):
	norma = norma + abs(z[i])**t

norma = norma**(1/t)

result = abs(norma)

print(round(result,7))



