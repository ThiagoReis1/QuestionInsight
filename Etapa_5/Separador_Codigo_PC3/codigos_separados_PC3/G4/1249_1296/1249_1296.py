#Phillip de Sousa Silva
#Av 06 , Ex 01

from numpy import*

I=array(eval(input("I:")))

A = min(I)
B = max(I)

C = 0.7 * A + 0.3 * B

D = 0.4 * A + 0.6 * B

a=0
b=0

for i in I:
	if (A <= i < C):
		a = a + 1
	if (C <= i < D):
		b = b + 1
		
J = array(zeros(2, dtype=int))

J[0]=a
J[1]=b

print(J)
		
