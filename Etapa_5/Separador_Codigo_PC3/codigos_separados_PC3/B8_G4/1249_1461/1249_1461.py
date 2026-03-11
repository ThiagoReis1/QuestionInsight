# Monalisa Pereira 21600560
# 250816
# Av 06 - Ex 01

from numpy import *

v = array(eval(input("Insira um vetor: ")))

A = min(v)
B = max(v)
C = 0.7*A+0.3*B
D = 0.4*A+0.6*B

x = array(zeros(2, dtype=int))

for i in v:
	if (i>=A) and (i<C):
		x[0] = x[0]+1
	elif (i>=C) and (i<D):
		x[1] = x[1]+1
		
print(x)