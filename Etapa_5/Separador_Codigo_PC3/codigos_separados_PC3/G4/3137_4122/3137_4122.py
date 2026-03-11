from numpy import*
from math import*
v=array(eval(input("numero n")))
n=(size(v))
p=0#variavel de posicao
ac=0#acumuladora
while(p<n):
	ac=ac+exp(v[p])
	p=p+1
M=log(ac/exp(n))
print(round(M,2))