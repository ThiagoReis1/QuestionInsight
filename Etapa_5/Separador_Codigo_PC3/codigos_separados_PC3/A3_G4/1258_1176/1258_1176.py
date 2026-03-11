from numpy import *
from math import *
p= float(input("Digite o numero: "))
while (p < 1):
	p= float(input("Digite o numero: "))
u = array(eval(input("Informe o vetor:")))
w = array(eval(input("Informe o vetor:")))
nu = 0.0
nw = 0.0
q= (p/p+1)
for i in range (size(u)):
	norma = norma(abs(u[i]**q))
	z = nu ** (1/q)
for i in range (size(w)):
	norma = norma(abs(w[i]**q))
	z = nw ** (1/q)	

print(round(nu+nw,3))
