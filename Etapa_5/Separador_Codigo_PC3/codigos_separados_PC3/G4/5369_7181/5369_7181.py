from numpy import *

cpf=array(eval(input("cpf:  ")))
i=0
aux=ones(size(cpf), dtype=int)
while(i<9):
	aux[i]=9-i
	i=i+1
i=0
sm=0
while(i<size(cpf)):
	sm=sm+cpf[i]*aux[i]
	i=i+1

print(sm%11)