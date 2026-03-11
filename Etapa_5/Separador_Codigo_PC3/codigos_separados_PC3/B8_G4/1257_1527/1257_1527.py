#ufam - Laís Amorim Reis - 21602327
from numpy import *

v = array(eval(input()))

A = min(v)
B = max(v)
C = 0.85*A + 0.15*B
D = 0.4*A + 0.6*B
x = array(zeros(2,dtype = int))
for i in range(0,size(v)):
	if(v[i]>=A and v[i]<C):
		x[0] = x[0]+1
	elif(v[i]>=D and v[i]<B):
		x[1] = x[1]+1
print(x)
	