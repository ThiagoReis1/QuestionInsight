from numpy import *

p = float(input("Digite o numero: "))
x = array(eval(input("Digite o vetor:")))
y = array(eval(input("Digite outro vetor")))

t = p /(p+1)
s=0

for i in range(size(x)):
	s+= abs(x[i]+y[i]) ** t

d=s**(1/t)

print(round(d, 3))
	