#Phillip de Sousa Silva
#Av 06 , Ex 02

from math import*

from numpy import*

p = eval(input("p:"))
I=array(eval(input("I:")))
J=array(eval(input("J:")))

t=p/(p+1)
q=0
q=t

K = array(zeros(size(I), dtype=float))

k=0

r=2
s=3
z=0

while (k<size(I)):
	n = r*I[k] + s*J[k]
	K[z]=n
	z=z+1
	k=k+1
print(K)

o=0

for i in K:
	o = abs(i)**q + o

d = (o)**1/(q)

print(round(d,7))