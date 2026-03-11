from numpy import *
cpf=array(eval(input("informe seu cpf:")))

aux=[9,8,7,6,5,4,3,2,1]

i=0
soma=0
while i< size(cpf):
	f1=cpf[i]*aux[i]
	soma=f1+soma
	i=i+1
dig=soma%11

print(dig)
	